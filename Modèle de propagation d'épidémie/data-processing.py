#!/usr/bin/python3

import seaborn as sns
import pandas as pd

from pylab import savefig


# ## boxplot quarantaine
# dataset = pd.read_csv('data/scenarios-quarantaine.txt')
# # print(dataset)

# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(5, 5))
# sns_plot = sns.boxplot(x="scenarios", y="(n  - count turtles with [state = 0])/ n", hue="Quarantaine", data=dataset, palette="Set1")
# sns_plot.set_xlabel("")
# sns_plot.set_ylabel("Taux de contamination")
# figure = sns_plot.get_figure()
# figure.savefig("effectiveness-of-quarantine.pdf")
# figure.savefig("effectiveness-of-quarantine.svg")

# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(5, 5))
# sns_plot = sns.boxplot(x="scenarios", y="[step]", hue="Quarantaine", data=dataset, palette="Set1")
# sns_plot.set_xlabel("")
# sns_plot.set_ylabel("Durée de l'épidemie (ticks)")
# figure = sns_plot.get_figure()
# figure.savefig("effectiveness-of-quarantine-duree.pdf")
# figure.savefig("effectiveness-of-quarantine-duree.svg")

# ## Quarantaine : dynamique
# dataset = pd.read_csv('data/scenarios-quarantaine-dynamique.txt')
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(5, 5))
# dataset_asymptomatique = dataset.loc[dataset['scenarios'] == "pop-asymptomatique"]
# sns_plot = sns.lineplot(x="[step]", y="count turtles with [state = 2]",  hue="Quarantaine",data=dataset_asymptomatique)
# sns_plot.set_xlabel("Temps (ticks)")
# sns_plot.set_ylabel("Nombre d'agents symptomatique")
# plt.savefig("dynamic-of-quarantine-pop-asymptomatique.pdf")
# plt.savefig("dynamic-of-quarantine-pop-asymptomatique.svg")

# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(5, 5))
# dataset_only_symptomatique = dataset.loc[dataset['scenarios'] == "pop-sans-asymptomatique"]
# sns_plot = sns.lineplot(x="[step]", y="count turtles with [state = 2]",  hue="Quarantaine",data=dataset_only_symptomatique)
# sns_plot.set_xlabel("Temps (ticks)")
# sns_plot.set_ylabel("Nombre d'agents symptomatique")
# plt.savefig("dynamic-of-quarantine-pop-sans-asymptomatique.pdf")
# plt.savefig("dynamic-of-quarantine-pop-sans-asymptomatique.svg")

# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(5, 5))
# dataset_1 = dataset.loc[dataset['scenarios'] == "pop-asymptomatique"]
# dataset_2 = dataset_1.loc[dataset_1['Quarantaine'] == "non"]
# dataset_3 = dataset.loc[dataset['scenarios'] == "pop-sans-asymptomatique"]
# dataset_4 = dataset_3.loc[dataset_3['Quarantaine'] == "non"]
# sns_plot = sns.lineplot(x="[step]", y="count turtles with [state = 2]", data=dataset_2, label="pop-asymptomatique")
# sns_plot = sns.lineplot(x="[step]", y="count turtles with [state = 2]", data=dataset_4, label="pop-sans-asymptomatique")
# sns_plot.set_xlabel("Temps (ticks)")
# sns_plot.set_ylabel("Nombre d'agents symptomatique")
# # plt.axvline(dataset_2.loc[dataset_2[["count turtles with [state = 2]"]].idxmax()]["[step]"].values, 0, dataset_2.loc[dataset_2[["count turtles with [state = 2]"]].idxmax()]["count turtles with [state = 2]"].values)
# # plt.axvline(dataset_4.loc[dataset_4[["count turtles with [state = 2]"]].idxmax()]["[step]"].values, 0, dataset_4.loc[dataset_4[["count turtles with [state = 2]"]].idxmax()]["count turtles with [state = 2]"].values)
# plt.savefig("dynamic-cmp-scenarios.pdf")
# plt.savefig("dynamic-cmp-scenarios.svg")



# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(5, 5))
# dataset_1 = dataset.loc[dataset['scenarios'] == "pop-asymptomatique"]
# dataset_2 = dataset_1.loc[dataset_1['Quarantaine'] == "non"]
# sns_plot = sns.lineplot(x="[step]", y="count turtles with [state = 1]", data=dataset_2, label="Asymptomatique")
# sns_plot = sns.lineplot(x="[step]", y="count turtles with [state = 2]", data=dataset_2, label="Symptomatique")
# sns_plot.set_xlabel("Temps (ticks)")
# sns_plot.set_ylabel("Nombre d'agents")
# plt.savefig("dynamic-of-infection-pop-asymptomatique.pdf")
# plt.savefig("dynamic-of-infection-pop-asymptomatique.svg")


# ## Couverture vaccinal
# dataset = pd.read_csv('data/exp1-couverture-vaccinale.txt')
# dataset_2 = dataset.loc[dataset['quarantaine'] == 1]
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(5, 5))
# sns_plot = sns.lineplot(x="p-vacciner", y="count turtles with [state = 3]/ n",  data=dataset_2, label="Avec quarantaine") #, ax=ax
# dataset_2 = dataset.loc[dataset['quarantaine'] == 0]
# sns_plot = sns.lineplot(x="p-vacciner", y="count turtles with [state = 3]/ n",  data=dataset_2, label="Sans quarantaine") #, ax=ax
# sns_plot.set_xlabel("Couverture vaccinale")
# sns_plot.set_ylabel("Proportion d'agents infecter")
# plt.grid(True, linestyle='--', linewidth=0.1, alpha=0.7)
# plt.savefig("couverture-vaccinale.pdf")
# plt.savefig("couverture-vaccinale.svg")


# ## Diagnostique rapide d'une maladie infectieuse
# dataset = pd.read_csv('data/exp1-diagnostic-rapide.txt')
# dataset_2 = dataset.loc[dataset['quarantaine'] == 1]
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(5, 5))
# sns_plot = sns.lineplot(x="p-diagnostique-rapide", y="count turtles with [state = 3] / n",  data=dataset_2, label="Avec quarantaine") #, ax=ax
# dataset_2 = dataset.loc[dataset['quarantaine'] == 0]
# sns_plot = sns.lineplot(x="p-diagnostique-rapide", y="count turtles with [state = 3] / n",  data=dataset_2, label="Sans quarantaine") #, ax=ax
# sns_plot.set_xlabel("Taux de diagnostique rapide journalier")
# sns_plot.set_ylabel("Proportion d'agents infecter")
# plt.grid(True, linestyle='--', linewidth=0.1, alpha=0.7)
# plt.savefig("diagnostique-rapide.pdf")
# plt.savefig("diagnostique-rapide.svg")

# ## Diagnostique rapide d'une maladie infectieuse
# dataset = pd.read_csv('data/exp1-diagnostic-rapide.txt')
# dataset_2 = dataset.loc[dataset['quarantaine'] == 1]
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(5, 5))
# sns_plot = sns.lineplot(x="p-diagnostique-rapide", y="[step]",  data=dataset_2, label="Avec quarantaine") #, ax=ax
# dataset_2 = dataset.loc[dataset['quarantaine'] == 0]
# sns_plot = sns.lineplot(x="p-diagnostique-rapide", y="[step]",  data=dataset_2, label="Sans quarantaine") #, ax=ax
# sns_plot.set_xlabel("Taux de diagnostique rapide journalier")
# sns_plot.set_ylabel("Durée de l'épidemie (ticks)")
# plt.grid(True, linestyle='--', linewidth=0.1, alpha=0.7)
# plt.savefig("diagnostique-rapide-duree-epidemie.pdf")
# plt.savefig("diagnostique-rapide-duree-epidemie.svg")

