import pandas as pd

data = {
    'Name': ['Ali', 'Sara', 'Mona', 'Omar'],
    'Math': [85, 90, 78, 92],
    'physics': [88, 76, 95, 89],
    'Chemistry': [90, 85, 88, 91]
}

print(pd.__version__)
df = pd.DataFrame(data)
print(df)
print("-----------------------------day 2: indexing and selection------------------------------")
print("\n")
print(df["Math"])
print("\n")
print(df[["Math"]])
print("\n")
print(df[["Math", "physics"]])
print("\n")
print(df.loc[0])
print("\n")
print(df.loc[0:2])
print("\n")
print("students with math score greater than 85:\n")
print(df[df["Math"] > 85])
print("\nstudents with physics score greater than 85:\n")
print(df[df["physics"] > 85])
print("students with math score greater than 85 and physics score greater than 85:\n")
print(df[ (df["Math"] > 85) & (df["physics"] > 85) ])
print("\nstudents with math score greater than 85 or physics Chemistry score greater than 90:\n")
print(df[ (df["Math"] > 85) | (df["Chemistry"] > 90) ])
print("\n-----------------------------day 3: sum, mean, std------------------------------\n")

# DataFrame:
#     Name    Math    physics    Chemistry
# 0   Ali     85       88         90
# 1   Sara    90       76         85
# 2   Mona    78       95         88
# 3   Omar    92       89         91

print("\nsum of Math, physics, and chemistry scores (from 400):")
print(df[["Math", "physics", "Chemistry"]].sum())
print("\nsum of every student scores (from 300):")
print(df[["Math", "physics", "Chemistry"]].sum(axis=1))
print("\nmean of Math, physics, chemistry scores:")
print(df[ ["Math", "physics", "Chemistry"]].mean())
print("\n mean of every student scores:")
print(df[ ["Math", "physics", "Chemistry"]].mean(axis=1))
print("\nstandard deviation of Math, physics, and chemistry scores:")
print(df[["Math", "physics", "Chemistry"]].std())
print("\nstandard deviation of every student scores:")
print(df[["Math", "physics", "Chemistry"]].std(axis=1))

print("\n-----------------------------day 4: add new column------------------------------\n")
# DataFrame:
#     Name    Math    physics    Chemistry
# 0   Ali     85       88         90
# 1   Sara    90       76         85
# 2   Mona    78       95         88
# 3   Omar    92       89         91
df["Total"] = df[["Math", "physics", "Chemistry"]].sum(axis=1)
print(df)
df["Average"] = df[["Math", "physics", "Chemistry"]].mean(axis=1)
print("\n", df)
print("\n-----------------day 5: apply function to column & description  & description all---------------------")
#    Name  Math  physics  Chemistry  Total    Average
# 0   Ali    85       88         90    263  87.666667
# 1  Sara    90       76         85    251  83.666667
# 2  Mona    78       95         88    261  87.000000
# 3  Omar    92       89         91    272  90.666667

df["Grade"] = df["Average"].apply(
    lambda x: "Excellent" if x >= 90
    else ("Very Good" if x >= 80
          else ("Good" if x >=70
                else "Pass")
          )
)
print("\n", df)

#    Name  Math  physics  Chemistry  Total    Average      Grade
# 0  Ali    85       88         90    263     87.666667  Very Good
# 1  Sara    90       76        85    251     83.666667  Very Good
# 2  Mona    78       95        88    261     87.000000  Very Good
# 3  Omar    92       89        91    272     90.666667  Excellent

print("\ndataframe info:", df.info())
print("\ndataframe description:\n", df.describe())
print("\ndataframe description of all columns:\n", df.describe(include='all'))