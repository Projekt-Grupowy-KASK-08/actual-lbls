import os, re, sys
import numpy as np
import pandas as pd
from utils import read_from_dat_file, preprocess_raw_data, remove_duplicates_from_list

INPUT_DIR = sys.path[0] + "/data/raw"
OUTPUT_DIR = sys.path[0] + "/data/preprocessed"
PROTOCOL_FILENAME = "protokoll.txt"

def process_mer_channels(inputDir, outputDir, siteInfo):
    """ Process .dat channel files from MER to create preprocessed .csv 
    
    Parameters
    ----------
    inputDir : str
        The directory of raw channels data from MER. Should contain only one site of probe.
    outputDir : str
        The directory with output of the program. Processing contains artifacts removal and data filtering.
    siteInfo : dir
        The dictionary containing information like probe's depth, quantisation etc.
    """

    channelPaths = list(map(lambda filename: os.path.join(inputDir, filename), siteInfo['recordFiles']))
   

    allChannelsData = []
    numberOfEntriesPerChannel = [] 
    for channelPath in channelPaths:
            raw_data = read_from_dat_file(channelPath)
            data = preprocess_raw_data(raw_data)
            
            numberOfEntriesPerChannel.append(len(data))
            allChannelsData.append(data)


    minEntries = min(numberOfEntriesPerChannel)
    numberOfEntriesPerChannel = [channelData[:minEntries] for channelData in allChannelsData]
    time_index = np.arange(0, minEntries / siteInfo['samplingRate'], 1.0 / siteInfo['samplingRate'])

    data = {
        "Time": time_index,
    }

    for i, channelData in enumerate(allChannelsData):
        channelName = siteInfo['channelsDesc'][i]
        data[channelName] = channelData[:minEntries]

    merFilename = os.path.basename(channelPaths[0])
    outputFilename = merFilename.replace("_CH1", "").replace(".dat", ".csv")
    outputPath = os.path.join(outputDir, outputFilename)
    pd.DataFrame(data=data).to_csv(outputPath, index=None)

def extractSiteInfo(siteText):
    """ Extracts information like depth of probe or sampling rate from site text

    Parameters
    ----------
    siteText : str
        The text of one probe's site from MER log/protocol. 
    
    Returns
    -------
    siteInfo : dict
        The dictionary containing information like probe's depth, quantisation etc.
    """
    depth_search = re.search(r'Depth: (.*) mm .+ Quantisation: (.*) Bit.+Sampling rate: (.*)Hz.*channel configuration:(.*?)\n.+', siteText, re.DOTALL)

    try:
        recordFiles = re.findall(r"[0-9]+_MER.*\.dat", siteText)
        siteInfo = {
            'depth': float(depth_search.group(1).replace(",", ".")),
            'quantisation': int(depth_search.group(2)),
            'samplingRate': int(depth_search.group(3)),
            'channelsDesc': depth_search.group(4).strip().split(", "),
            'recordFiles': remove_duplicates_from_list(recordFiles)
        }
        return siteInfo
    except Exception as e:
        print("ERROR: Could not process site!")
        print(e)
    
    

def process_patients(inputDir, outputDir, logFilename):
    """ Process patient files from MER  
    
    Parameters
    ----------
    inputDir : str
        The directory with location of raw patients data from MER. Should contain patients and in each MER recording(s) should be placed in separate directories.
    outputDir : str
        The directory with output of the program. Processing includes artifacts removal and data filtering. Directories structure is preserved. Directory is created if does not exist. 
    logFilename : str
        Filename of file with information about MER e.g. sampling rate, quantisation and depth of probe 
    """

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    
    patientsDirectories = os.listdir(inputDir)
    patientsNumber = len(patientsDirectories)

    for i, patientName in enumerate(patientsDirectories):
        print(f"Processing {patientName} ({i+1}/{patientsNumber})...")
        patientPath = os.path.join(inputDir, patientName)

        for merId in os.listdir(patientPath):
            merIdPath = os.path.join(patientPath, merId)
            outputDirPath = os.path.join(outputDir, patientName, merId)
            if not os.path.exists(outputDirPath):
                os.makedirs(outputDirPath)

            logFilePath = os.path.join(merIdPath, logFilename)
            sitesText = ""
            with open(logFilePath, "r") as logFile:
                sitesText = re.findall(r"New site no .+? -{42}", logFile.read(), re.DOTALL)
            
            sitesInfo = map(extractSiteInfo, sitesText) 
            for siteInfo in sitesInfo:
                process_mer_channels(merIdPath, outputDirPath, siteInfo)

process_patients(INPUT_DIR, OUTPUT_DIR, PROTOCOL_FILENAME)