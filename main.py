import salmontracker
from salmontracker import (
    initAll,
    initUser,
    findPlayerIdByName,
    hasPlayer,
    withoutPlayer,
    findRotationByWeaponsAndStage,
    duringRotationInt,
    notDuringRotationInt,
    hasWeapon,
    doesntHaveWeapon,
    onStage,
    notOnStage,
    usesWeapon,
    doesntUseWeapon,
    dangerRate,
    notDangerRate,
    greaterThanDangerRate,
    notGreaterThanDangerRate,
    lessThanDangerRate,
    notLessThanDangerRate,
    clearWave,
    notClearWave,
    greaterThanClearWave,
    notGreaterThanClearWave,
    lessThanClearWave,
    notLessThanClearWave,
    withSpecial,
    withoutSpecial
)
import json
from typing import List, Tuple
import sys
import os
import jsonlines


def filterBy(paths: List[str], dataFile: List[str]) -> List[Tuple[str, str]]:
    filters: List[Tuple[str, str]] = []
    print()
    print("Rotation")
    print("Player")
    print("Has Weapon")
    print("Uses Weapon")
    print("Stage")
    print("Danger Rate")
    print()
    stat: str = input("Choose a stat to run analysis on: ")
    if stat == "Player":
        playerName = input("Enter a player name to run analysis on: ")
        playerId: List[str] = findPlayerIdByName(paths[0], dataFile[0], playerName)
        print(playerId)
        val: str = playerId[int(input("Pick the player id by index: "))]
        mode: str = input("Choose whether you want With, Without, or Both: ")
        for i in range(0, len(paths)):
            if mode == "With":
                filters.append(hasPlayer(paths[i], dataFile[i], val))
            elif mode == "Without":
                filters.append(withoutPlayer(paths[i], dataFile[i], val))
            elif mode == "Both":
                filters.append(hasPlayer(paths[i], dataFile[i], val))
                filters.append(withoutPlayer(paths[i], dataFile[i], val))
            else:
                sys.exit()
    elif stat == "Rotation":
        weapons = []
        for i in range(0, 4):
            weapons.append(input("Enter a weapon: "))
        stageChoice = input("Enter the stage: ")
        rotations: List[int] = findRotationByWeaponsAndStage(
            paths[0] + dataFile[0], weapons, stageChoice
        )
        print(rotations)
        rot: int = rotations[int(input("Pick the rotation id by index: "))]
        mode = input("Choose whether you want With, Without, or Both: ")
        for i in range(0, len(paths)):
            if mode == "With":
                filters.append(duringRotationInt(paths[i], dataFile[i], rot))
            elif mode == "Without":
                filters.append(notDuringRotationInt(paths[i], dataFile[i], rot))
            elif mode == "Both":
                filters.append(duringRotationInt(paths[i], dataFile[i], rot))
                filters.append(notDuringRotationInt(paths[i], dataFile[i], rot))
            else:
                sys.exit()
    elif stat == "Has Weapon":
        val = input("Enter a weapon: ")
        mode = input("Choose whether you want With, Without, or Both: ")
        for i in range(0, len(paths)):
            if mode == "With":
                filters.append(hasWeapon(paths[i], dataFile[i], val))
            elif mode == "Without":
                filters.append(doesntHaveWeapon(path[i], dataFile[i], val))
            elif mode == "Both":
                filters.append(hasWeapon(path[i], dataFile[i], val))
                filters.append(doesntHaveWeapon(path, dataFile[i], val))
            else:
                sys.exit()
    elif stat == "Uses Weapon":
        val = input("Enter a weapon: ")
        mode = input("Choose whether you want With, Without, or Both: ")
        for i in range(0, len(paths)):
            if mode == "With":
                filters.append(usesWeapon(paths[i], dataFile[i], val))
            elif mode == "Without":
                filters.append(doesntUseWeapon(path[i], dataFile[i], val))
            elif mode == "Both":
                filters.append(usesWeapon(path[i], dataFile[i], val))
                filters.append(doesntUseWeapon(path, dataFile[i], val))
            else:
                sys.exit()
    elif stat == "Stage":
        val = input("Enter a stage: ")
        mode = input("Choose whether you want With, Without, or Both: ")
        for i in range(0, len(paths)):
            if mode == "With":
                filters.append(onStage(paths[i], dataFile[i], val))
            elif mode == "Without":
                filters.append(notOnStage(path[i], dataFile[i], val))
            elif mode == "Both":
                filters.append(onStage(paths[i], dataFile[i], val))
                filters.append(notOnStage(paths[i], dataFile[i], val))
            else:
                sys.exit()
    elif stat == "Danger Rate":
        comparison: str = input("Choose whether you want =, >, or <: ")
        val = input("Enter the danger rate: ")
        mode = input("Choose whether you want With, Without, or Both: ")
        for i in range(0, len(paths)):
            if mode == "With":
                if comparison == "=":
                    filters.append(dangerRate(paths[i], dataFile[i], val))
                elif comparison == ">":
                    filters.append(greaterThanDangerRate(paths[i], dataFile[i], val))
                elif comparison == "<":
                    filters.append(lessThanDangerRate(paths[i], dataFile[i], val))
                else:
                    sys.exit()
            elif mode == "Without":
                if comparison == "=":
                    filters.append(notDangerRate(paths[i], dataFile[i], val))
                elif comparison == ">":
                    filters.append(notGreaterThanDangerRate(paths[i], dataFile[i], val))
                elif comparison == "<":
                    filters.append(notLessThanDangerRate(paths[i], dataFile[i], val))
                else:
                    sys.exit()
            elif mode == "Both":
                if comparison == "=":
                    filters.append(dangerRate(paths[i], dataFile[i], val))
                    filters.append(notDangerRate(paths[i], dataFile[i], val))
                elif comparison == ">":
                    filters.append(greaterThanDangerRate(paths[i], dataFile[i], val))
                    filters.append(notGreaterThanDangerRate(paths[i], dataFile[i], val))
                elif comparison == "<":
                    filters.append(lessThanDangerRate(paths[i], dataFile[i], val))
                    filters.append(notLessThanDangerRate(paths[i], dataFile[i], val))
                else:
                    sys.exit()
            else:
                sys.exit()
    elif stat == "Clear Wave":
        comparison = input("Choose whether you want =, >, or <: ")
        wave: int = int(input("Enter the clear wave: "))
        mode = input("Choose whether you want With, Without, or Both: ")
        for i in range(0, len(paths)):
            if mode == "With":
                if comparison == "=":
                    filters.append(clearWave(paths[i], dataFile[i], wave))
                elif comparison == ">":
                    filters.append(greaterThanClearWave(paths[i], dataFile[i], wave))
                elif comparison == "<":
                    filters.append(lessThanClearWave(paths[i], dataFile[i], wave))
                else:
                    sys.exit()
            elif mode == "Without":
                if comparison == "=":
                    filters.append(notClearWave(paths[i], dataFile[i], wave))
                elif comparison == ">":
                    filters.append(notGreaterThanClearWave(paths[i], dataFile[i], wave))
                elif comparison == "<":
                    filters.append(notLessThanClearWave(paths[i], dataFile[i], wave))
                else:
                    sys.exit()
            elif mode == "Both":
                if comparison == "=":
                    filters.append(clearWave(paths[i], dataFile[i], wave))
                    filters.append(notClearWave(paths[i], dataFile[i], wave))
                elif comparison == ">":
                    filters.append(greaterThanClearWave(paths[i], dataFile[i], wave))
                    filters.append(notGreaterThanClearWave(paths[i], dataFile[i], wave))
                elif comparison == "<":
                    filters.append(lessThanClearWave(paths[i], dataFile[i], wave))
                    filters.append(notLessThanClearWave(paths[i], dataFile[i], wave))
                else:
                    sys.exit()
            else:
                sys.exit()
    elif stat == "special":
        val = input("Enter the danger rate: ")
        mode = input("Choose whether you want With, Without, or Both: ")
        for i in range(0, len(paths)):
            if mode == "With":
                filters.append(withSpecial(paths[i], dataFile[i], val))
            elif mode == "Without":
                filters.append(withoutSpecial(paths[i], dataFile[i], val))
            elif mode == "Both":
                filters.append(withSpecial(paths[i], dataFile[i], val))
                filters.append(withoutSpecial(paths[i], dataFile[i], val))
            else:
                sys.exit()
    else:
        sys.exit()
    return filters


def printOverview(paths: List[str], dataFile: List[str]):
    which = input("Would you like to print a SpecificList or AllLists: ")
    if which == "AllLists":
        for i in range(0, len(paths)):
            salmontracker.printOverview(paths[i], dataFile[i])
    elif which == "SpecificList":
        for i in range(0, len(paths)):
            print(paths[i] + dataFile[i])
        chosenList = int(input("Which list (by index): "))
        salmontracker.printOverview(paths[chosenList], dataFile[chosenList])
        print()
    else:
        sys.exit()


def printAllJobs(path: str, dataFile: str):
    with jsonlines.open(path + dataFile, mode="r") as reader:
        for job in reader:
            salmontracker.printGeneral(job)
            print()
            salmontracker.printWaves(job)
            print()
            salmontracker.printPlayers(job)
            print()
            salmontracker.printBosses(job)
            print()
            print()


def printJobs(paths: List[str], dataFile: List[str]):
    which = input("Would you like to print from a SpecificList or AllLists: ")
    if which == "AllLists":
        for i in range(0, len(paths)):
            salmontracker.printOverview(paths[i], dataFile[i])


def processData(paths: List[str], dataFile: List[str]):
    print()
    print("PrintOverview")
    print("PrintJobs")
    print("HypothesisTesting")
    print("Quit")
    mode: str = input("What would you like to do?")
    while mode != "Quit":
        if mode == "PrintOverview":
            printOverview(paths, dataFile)
        elif mode == "PrintJobs":
            printJobs(paths, dataFile)
        else:
            sys.exit()
        print()
        print("PrintOverview")
        print("PrintJobs")
        print("HypothesisTesting")
        print("Quit")
        mode = input("What would you like to do?")


print("All")
print("User")
scope: str = input("Pick an analysis scope: ")
path: str = ""
data: str = ""
if scope == "All":
    dataFileStart = initAll()
    path = dataFileStart[0]
    data = dataFileStart[1]
elif scope == "User":
    dataFileStart = initUser(json.load(open("keys.json", "r"))["statink_key"])
    path = dataFileStart[0]
    data = dataFileStart[1]
else:
    sys.exit()
currentPaths: List[str] = []
allPaths: List[str] = []
dataFiles: List[str] = []
allFiles: List[str] = []
while input("Add a filter (Y/N): ") == "Y":
    if currentPaths == []:
        filtered: List[Tuple[str, str]] = filterBy([path], [data])
        for f in filtered:
            currentPaths.append(f[0])
            dataFiles.append(f[1])
            allPaths.append(f[0])
            allFiles.append(f[1])
    else:
        filtered = filterBy(currentPaths, dataFiles)
        currentPaths = []
        dataFiles = []
        for f in filtered:
            currentPaths.append(f[0])
            dataFiles.append(f[1])
            allPaths.append(f[0])
            allFiles.append(f[1])
processData(currentPaths, dataFiles)
if input("Clean (Y/N): ") == "Y":
    for a in range(0, len(allPaths)):
        os.remove(allPaths[a] + allFiles[a])