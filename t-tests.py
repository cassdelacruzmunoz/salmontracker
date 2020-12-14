from salmontracker import init, findPlayerIdByName, hasPlayer, withoutPlayer, findRotationByWeaponsAndStage, duringRotationInt, notDuringRotationInt, hasWeapon, doesntHaveWeapon, onStage, notOnStage, getArrayOfStat, getArrayOfStat2D
from scipy.stats import ttest_ind
import numpy as np
import matplotlib.pyplot as plt

data = init()
print("Rotation")
print("Player")
print("Weapon")
print("Stage")
stat = input("Choose a stat to run analysis on: ")
val = ""
withVal = []
withoutVal = []
if stat == "Player":
    playerId = findPlayerIdByName(data, input("Enter a player name to run analysis on: "))
    print(playerId)
    val = playerId[int(input("Pick the player id by index: "))]
    withVal = list(filter(hasPlayer(val), data))
    withoutVal = list(filter(withoutPlayer(val), data))
elif stat == "Rotation":
    weapons = []
    for i in range(0, 4):
        weapons.append(input("Enter a weapon: "))
    stageChoice = input("Enter the stage: ")
    rotations = findRotationByWeaponsAndStage(data, weapons, stageChoice)
    print(rotations)
    val = rotations[int(input("Pick the rotation id by index: "))]
    withVal = list(filter(duringRotationInt(val), data))
    withoutVal = list(filter(notDuringRotationInt(val), data))
elif stat == "Weapon":
    val = input("Enter a weapon: ")
    withVal = list(filter(hasWeapon(val), data))
    withoutVal = list(filter(doesntHaveWeapon(val), data))
elif stat == "Stage":
    val = input("Enter a stage: ")
    withVal = list(filter(onStage(val), data))
    withoutVal = list(filter(notOnStage(val), data))
else:
    exit()
withValClearWaves = getArrayOfStat(withVal, "clear_waves")
withoutValClearWaves = getArrayOfStat(withoutVal, "clear_waves")
t, p = ttest_ind(withValClearWaves, withoutValClearWaves, equal_var=False)
print("a - b = " + str(np.mean(withValClearWaves) - np.mean(withoutValClearWaves)))
print("t = " + str(t))
print("p = " + str(p))
print()
withValDangerRate = getArrayOfStat(withVal, "danger_rate")
withoutValDangerRate = getArrayOfStat(withoutVal, "danger_rate")
t, p = ttest_ind(withValDangerRate, withoutValDangerRate, equal_var=False)
plt.figure(1)
plt.subplot(121)
plt.hist(withValDangerRate, density=True)
plt.xlabel('Danger Rate')
plt.ylabel('Probability')
plt.subplot(122)
plt.hist(withoutValDangerRate, density=True)
plt.xlabel('Danger Rate')
plt.ylabel('Probability')
print("a - b = " + str(np.mean(withValDangerRate) - np.mean(withoutValDangerRate)))
print("t = " + str(t))
print("p = " + str(p))
print()
withValGoldenTotal = getArrayOfStat2D(withVal, "my_data", "golden_egg_delivered")
withoutValGoldenTotal = getArrayOfStat2D(withoutVal, "my_data", "golden_egg_delivered")
t, p = ttest_ind(withValGoldenTotal, withoutValGoldenTotal, equal_var=False)
plt.figure(2)
plt.subplot(121)
plt.hist(withValGoldenTotal, density=True)
plt.xlabel('Golden Eggs')
plt.ylabel('Probability')
plt.subplot(122)
plt.hist(withoutValGoldenTotal, density=True)
plt.xlabel('Golden Eggs')
plt.ylabel('Probability')
print("a - b = " + str(np.mean(withValGoldenTotal) - np.mean(withoutValGoldenTotal)))
print("t = " + str(t))
print("p = " + str(p))
print()
withValPowerTotal = getArrayOfStat2D(withVal, "my_data", "power_egg_collected")
withoutValPowerTotal = getArrayOfStat2D(withoutVal, "my_data", "power_egg_collected")
t, p = ttest_ind(withValPowerTotal, withoutValPowerTotal, equal_var=False)
plt.figure(3)
plt.subplot(121)
plt.hist(withValPowerTotal, density=True)
plt.xlabel('Power Eggs')
plt.ylabel('Probability')
plt.subplot(122)
plt.hist(withoutValPowerTotal, density=True)
plt.xlabel('Power Eggs')
plt.ylabel('Probability')
print("a - b = " + str(np.mean(withValPowerTotal) - np.mean(withoutValPowerTotal)))
print("t = " + str(t))
print("p = " + str(p))
print()
plt.show()
