import core
import sort_by_stat
from core import (
    findPlayerIdByName,
    hasPlayer,
    findRotationByWeaponsAndStage,
    duringRotationInt,
    hasWeapon,
    onStage,
    usesWeapon,
    dangerRate,
    notDangerRate,
    greaterThanDangerRate,
    notGreaterThanDangerRate,
    lessThanDangerRate,
    notLessThanDangerRate,
    clearWave,
    greaterThanClearWave,
    lessThanClearWave,
    notLessThanClearWave,
    withSpecial,
)
import ujson
from typing import List, Tuple
import sys
import os
import jsonlines
from scipy.stats import ttest_ind
import numpy as np
import matplotlib.pyplot as plt
import gzip


def filterBy(paths: List[str], dataFile: List[str]) -> List[Tuple[str, str]]:
    filters: List[Tuple[str, str]] = []
    print()
    print("Rotation")
    print("Player")
    print("Has Weapon")
    print("Uses Weapon")
    print("Stage")
    print("Danger Rate")
    print("Clear Wave")
    print("Special")
    stat: str = input("Choose an attribute to run filter on: ")
    if stat == "Player":
        playerName: str = input("Enter a player name to run analysis on: ")
        playerId: List[str] = findPlayerIdByName(paths[0] + dataFile[0], playerName)
        print(playerId)
        val: str = playerId[int(input("Pick the player id by index: "))]
        mode: str = input("Choose whether you want [With/Without/Both]: ")
        clearAfter: str = input("Choose whether you would like to clear after [Y/N]:")
        for i in range(0, len(paths)):
            if mode == "With":
                filters.append(hasPlayer(paths[i], dataFile[i], val)[0])
                os.remove(paths[i] + dataFile[i][:-6] + "/notPlayer/" + val + ".jl.gz")
            elif mode == "Without":
                filters.append(hasPlayer(paths[i], dataFile[i], val)[1])
                os.remove(paths[i] + dataFile[i][:-6] + "/player/" + val + ".jl.gz")
            elif mode == "Both":
                result: Tuple[Tuple[str, str], Tuple[str, str]] = hasPlayer(
                    paths[i], dataFile[i], val
                )
                filters.append(result[0])
                filters.append(result[1])
            else:
                sys.exit()
            if clearAfter == "Y" and paths[i] != "data/":
                os.remove(paths[i] + dataFile[i])
    elif stat == "Rotation":
        weapons: List[str] = []
        for i in range(0, 4):
            weapons.append(input("Enter a weapon: "))
        stageChoice: str = input("Enter the stage: ")
        rotations: List[int] = findRotationByWeaponsAndStage(
            paths[0] + dataFile[0], weapons, stageChoice
        )
        print(rotations)
        rot: int = rotations[int(input("Pick the rotation id by index: "))]
        mode = input("Choose whether you want [With/Without/Both]: ")
        clearAfter = input("Choose whether you would like to clear after [Y/N]: ")
        for i in range(0, len(paths)):
            if mode == "With":
                filters.append(duringRotationInt(paths[i], dataFile[i], rot)[0])
                os.remove(path + data[0:-6] + "/notRotation/" + str(rot) + ".jl.gz")
            elif mode == "Without":
                filters.append(duringRotationInt(paths[i], dataFile[i], rot)[1])
                os.remove(path + data[0:-6] + "/rotation/" + str(rot) + ".jl.gz")
            elif mode == "Both":
                result = duringRotationInt(paths[i], dataFile[i], rot)
                filters.append(result[0])
                filters.append(result[1])
            else:
                sys.exit()
            if clearAfter == "Y" and paths[i] != "data/":
                os.remove(paths[i] + dataFile[i])
    elif stat == "Has Weapon":
        val = input("Enter a weapon: ")
        mode = input("Choose whether you want [With/Without/Both]: ")
        clearAfter = input("Choose whether you would like to clear after [Y/N]:")
        for i in range(0, len(paths)):
            if mode == "With":
                filters.append(hasWeapon(paths[i], dataFile[i], val)[0])
                os.remove(path + data[0:-6] + "/notWeapon/" + val + ".jl.gz")
            elif mode == "Without":
                filters.append(hasWeapon(paths[i], dataFile[i], val)[1])
                os.remove(path + data[0:-6] + "/weapon/" + val + ".jl.gz")
            elif mode == "Both":
                result = hasWeapon(paths[i], dataFile[i], val)
                filters.append(result[0])
                filters.append(result[1])
            else:
                sys.exit()
            if clearAfter == "Y" and paths[i] != "data/":
                os.remove(paths[i] + dataFile[i])
    elif stat == "Uses Weapon":
        val = input("Enter a weapon: ")
        mode = input("Choose whether you want [With/Without/Both]: ")
        clearAfter = input("Choose whether you would like to clear after [Y/N]:")
        for i in range(0, len(paths)):
            if mode == "With":
                filters.append(usesWeapon(paths[i], dataFile[i], val)[0])
                os.remove(path + data[0:-6] + "/notUsesWeapon/" + val + ".jl.gz")
            elif mode == "Without":
                filters.append(usesWeapon(paths[i], dataFile[i], val)[1])
                os.remove(path + data[0:-6] + "/usesWeapon/" + val + ".jl.gz")
            elif mode == "Both":
                result = usesWeapon(paths[i], dataFile[i], val)
                filters.append(result[0])
                filters.append(result[1])
            else:
                sys.exit()
            if clearAfter == "Y" and paths[i] != "data/":
                os.remove(paths[i] + dataFile[i])
    elif stat == "Stage":
        val = input("Enter a stage: ")
        mode = input("Choose whether you want [With/Without/Both]: ")
        clearAfter = input("Choose whether you would like to clear after [Y/N]:")
        for i in range(0, len(paths)):
            if mode == "With":
                filters.append(onStage(paths[i], dataFile[i], val)[0])
                os.remove(path + data[0:-6] + "/notStage/" + val + ".jl.gz")
            elif mode == "Without":
                filters.append(onStage(paths[i], dataFile[i], val)[1])
                os.remove(path + data[0:-6] + "/stage/" + val + ".jl.gz")
            elif mode == "Both":
                result = onStage(paths[i], dataFile[i], val)
                filters.append(result[0])
                filters.append(result[1])
            else:
                sys.exit()
            if clearAfter == "Y" and paths[i] != "data/":
                os.remove(paths[i] + dataFile[i])
    elif stat == "Danger Rate":
        comparison: str = input("Choose whether you want [=/>/<]: ")
        val = input("Enter the danger rate: ")
        mode = input("Choose whether you want [With/Without/Both]: ")
        clearAfter = input("Choose whether you would like to clear after [Y/N]:")
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
            if clearAfter == "Y" and paths[i] != "data/":
                os.remove(paths[i] + dataFile[i])
    elif stat == "Clear Wave":
        comparison = input("Choose whether you want [=/>/<]: ")
        wave: int = int(input("Enter the clear wave: "))
        mode = input("Choose whether you want [With/Without/Both]: ")
        clearAfter = input("Choose whether you would like to clear after [Y/N]:")
        for i in range(0, len(paths)):
            if mode == "With":
                if comparison == "=":
                    filters.append(clearWave(paths[i], dataFile[i], wave)[0])
                    os.remove(
                        path
                        + data[0:-6]
                        + "/clearWaves/notEqual/"
                        + str(wave)
                        + ".jl.gz"
                    )
                elif comparison == ">":
                    filters.append(greaterThanClearWave(paths[i], dataFile[i], wave)[0])
                    os.remove(
                        path
                        + data[0:-6]
                        + "/clearWaves/notGreaterThan/"
                        + str(wave)
                        + ".jl.gz"
                    )
                elif comparison == "<":
                    filters.append(lessThanClearWave(paths[i], dataFile[i], wave))
                else:
                    sys.exit()
            elif mode == "Without":
                if comparison == "=":
                    filters.append(clearWave(paths[i], dataFile[i], wave)[1])
                    os.remove(
                        path + data[0:-6] + "/clearWaves/equal/" + str(wave) + ".jl.gz"
                    )
                elif comparison == ">":
                    filters.append(greaterThanClearWave(paths[i], dataFile[i], wave)[1])
                    os.remove(
                        path
                        + data[0:-6]
                        + "/clearWaves/greaterThan/"
                        + str(wave)
                        + ".jl.gz"
                    )
                elif comparison == "<":
                    filters.append(notLessThanClearWave(paths[i], dataFile[i], wave))
                else:
                    sys.exit()
            elif mode == "Both":
                if comparison == "=":
                    result = clearWave(paths[i], dataFile[i], wave)
                elif comparison == ">":
                    result = greaterThanClearWave(paths[i], dataFile[i], wave)
                elif comparison == "<":
                    filters.append(lessThanClearWave(paths[i], dataFile[i], wave))
                    filters.append(notLessThanClearWave(paths[i], dataFile[i], wave))
                else:
                    sys.exit()
                filters.append(result[0])
                filters.append(result[1])
            else:
                sys.exit()
            if clearAfter == "Y" and paths[i] != "data/":
                os.remove(paths[i] + dataFile[i])
    elif stat == "Special":
        val = input("Enter the special: ")
        mode = input("Choose whether you want [With/Without/Both]: ")
        clearAfter = input("Choose whether you would like to clear after [Y/N]:")
        for i in range(0, len(paths)):
            if mode == "With":
                filters.append(withSpecial(paths[i], dataFile[i], val)[0])
                os.remove(path + data[0:-6] + "/notSpecial/" + val + ".jl.gz")
            elif mode == "Without":
                filters.append(withSpecial(paths[i], dataFile[i], val)[0])
                os.remove(path + data[0:-6] + "/special/" + val + ".jl.gz")
            elif mode == "Both":
                result = withSpecial(paths[i], dataFile[i], val)
                filters.append(result[0])
                filters.append(result[1])
            else:
                sys.exit()
            if clearAfter == "Y" and paths[i] != "data/":
                os.remove(paths[i] + dataFile[i])
    else:
        sys.exit()
    return filters


def printOverview(paths: List[str], dataFile: List[str]):
    which: str = input("Would you like to print a [SpecificList/AllLists]: ")
    if which == "AllLists":
        for i in range(0, len(paths)):
            core.printOverview(paths[i] + dataFile[i])
    elif which == "SpecificList":
        for i in range(0, len(paths)):
            print(paths[i] + dataFile[i])
        chosenList: int = int(input("Which list (by index): "))
        core.printOverview(paths[chosenList] + dataFile[chosenList])
        print()
    else:
        sys.exit()


def printAllJobs(dataFile: str):
    with gzip.open(dataFile) as reader:
        for job in jsonlines.Reader(reader, loads=ujson.loads):
            core.printGeneral(job)
            print()
            core.printWaves(job)
            print()
            core.printPlayers(job)
            print()
            core.printBosses(job)
            print()
            print()


def printJobs(paths: List[str], dataFile: List[str]):
    which: str = input("Would you like to print from a SpecificList or AllLists: ")
    if which == "AllLists":
        for i in range(0, len(paths)):
            printAllJobs(paths[i] + dataFile[i])
    elif which == "SpecificList":
        for i in range(0, len(paths)):
            print(paths[i] + dataFile[i])
        chosenList: int = int(input("Which list (by index): "))
        printAllJobs(paths[chosenList] + dataFile[chosenList])
    else:
        sys.exit()


def hypothesisTesting(paths: List[str], dataFile: List[str]):
    for i in range(0, len(paths)):
        print(paths[i] + dataFile[i])
    first: int = int(input("Which is the first list you'd like to use (by index): "))
    second: int = int(input("Which is the first list you'd like to use (by index): "))
    stat: str = input("Which stat would you like to test: ")
    firstStat: List[float] = core.getArrayOfStat(paths[first] + dataFile[first], stat)
    secondStat: List[float] = core.getArrayOfStat(
        paths[second] + dataFile[second], stat
    )
    t, p = ttest_ind(firstStat, secondStat, equal_var=False)
    print("a - b = " + str(np.mean(firstStat) - np.mean(secondStat)))
    print("t = " + str(t))
    print("p = " + str(p))
    plt.subplot(121)
    plt.hist(firstStat, density=True)
    plt.xlabel(stat)
    plt.ylabel("Probability")
    plt.subplot(122)
    plt.hist(secondStat, density=True)
    plt.xlabel(stat)
    plt.ylabel("Probability")
    plt.show()


def sortAttributeByStat(paths: List[str], dataFile: List[str]):
    which: str = input("Would you like to print from a [SpecificList/AllLists]: ")
    stat: str = input("Enter a stat to sort by: ")
    mode: str = input("Pick a mode [Stage/Weapon/Rotation/Special]: ")
    if which == "AllLists":
        for i in range(0, len(paths)):
            if mode == "Stage":
                sort_by_stat.sortStages(paths[i] + dataFile[i], stat)
            elif mode == "Weapon":
                sort_by_stat.sortWeapons(paths[i], dataFile[i], stat)
            elif mode == "Rotation":
                sort_by_stat.sortRotation(paths[i], dataFile[i], stat)
            elif mode == "Special":
                sort_by_stat.sortSpecial(paths[i] + dataFile[i], stat)
            else:
                sys.exit()
    elif which == "SpecificList":
        for i in range(0, len(paths)):
            print(paths[i] + dataFile[i])
        chosenList: int = int(input("Which list (by index): "))
        if mode == "Stage":
            sort_by_stat.sortStages(paths[chosenList] + dataFile[chosenList], stat)
        elif mode == "Weapon":
            sort_by_stat.sortWeapons(paths[chosenList], dataFile[chosenList], stat)
        elif mode == "Rotation":
            sort_by_stat.sortRotation(paths[chosenList], dataFile[chosenList], stat)
        elif mode == "Special":
            sort_by_stat.sortSpecial(paths[chosenList] + dataFile[chosenList], stat)
        else:
            sys.exit()
    else:
        sys.exit()


def waveClearPercentageWithWeapon(paths: List[str], dataFile: List[str]):
    which: str = input("Would you like to print from [SpecificList/AllLists]: ")
    weapon: str = input("Enter a weapon to test: ")
    if which == "AllLists":
        for i in range(0, len(paths)):
            print(
                weapon
                + ": "
                + str(
                    core.waveClearPercentageWithWeapon(paths[i] + dataFile[i], weapon)
                )
            )
    elif which == "SpecificList":
        for i in range(0, len(paths)):
            print(paths[i] + dataFile[i])
        chosenList = int(input("Which list (by index): "))
        core.waveClearPercentageWithWeapon(
            paths[chosenList] + dataFile[chosenList], weapon
        )
        print()
    else:
        sys.exit()


def processData(paths: List[str], dataFile: List[str]):
    print()
    print("PrintOverview")
    print("PrintJobs")
    print("HypothesisTesting")
    print("SortAttributeByStat")
    print("WaveClearPercentageWithWeapon")
    print("Quit")
    mode: str = input("What would you like to do: ")
    while mode != "Quit":
        if mode == "PrintOverview":
            printOverview(paths, dataFile)
        elif mode == "PrintJobs":
            printJobs(paths, dataFile)
        elif mode == "HypothesisTesting":
            hypothesisTesting(paths, dataFile)
        elif mode == "SortAttributeByStat":
            pass
        elif mode == "WaveClearPercentageWithWeapon":
            waveClearPercentageWithWeapon(paths, dataFile)
        else:
            sys.exit()
        print()
        print("PrintOverview")
        print("PrintJobs")
        print("HypothesisTesting")
        print("SortAttributeByStat")
        print("WaveClearPercentageWithWeapon")
        print("Quit")
        mode = input("What would you like to do: ")


if __name__ == "__main__":
    print("All")
    print("User")
    scope: str = input("Pick an analysis scope: ")
    dataFileStart: Tuple[str, str] = core.init(
        scope, ujson.load(open("keys.json", "r"))["statink_key"]
    )
    path: str = dataFileStart[0]
    data: str = dataFileStart[1]
    currentPaths: List[str] = [path]
    allPaths: List[str] = []
    dataFiles: List[str] = [data]
    allFiles: List[str] = []
    while input("Add a filter [Y/N]: ") == "Y":
        filtered = filterBy(currentPaths, dataFiles)
        currentPaths = []
        dataFiles = []
        for f in filtered:
            currentPaths.append(f[0])
            dataFiles.append(f[1])
            allPaths.append(f[0])
            allFiles.append(f[1])
    processData(currentPaths, dataFiles)
    if input("Clean [Y/N] (only if you didn't use clearAfter): ") == "Y":
        for a in range(0, len(allPaths)):
            os.remove(allPaths[a] + allFiles[a])
