import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. simple plot with 4 numbers
plt.plot([1, 3, 2, 4])
plt.show()

# 2. points have x and y values; add title and axis labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Test Plot', fontsize=8, color='g')
plt.xlabel('number n')
plt.ylabel('n^2')
plt.show()

# 3. change figure size. plot red dots; set axis scales x: 0-6 and y: 0-20
plt.figure(figsize=(1,5))	# 1 inch wide x 5 inches tall
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')	# red-o
plt.axis([0, 6, 0, 20])						# [xmin, xmax, ymin, ymax]
plt.annotate('square it', (3,6))
plt.show()

# 4. bar chart with four bars
plt.clf()			# clear figure
x = np.arange(4)
y = [8.8, 5.2, 3.6, 5.9]
plt.xticks(x, ('Ankit', 'Hans', 'Joe', 'Flaco'))
plt.bar(x, y)
# plt.bar(x, y, color='y')
# plt.bar(x, y, color=['lime', 'r', 'k', 'tan'])
plt.show()

# 5. two sets of 10 random dots plotted
d = {'Red O' : np.random.rand(10),
     'Grn X' : np.random.rand(10)}
df = pd.DataFrame(d)
df.plot(style=['ro','gx'])
plt.show()

# 6. time series - six months of random floats
ts = pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018', periods=180))
df = pd.DataFrame(np.random.randn(180, 3), index=ts.index, columns=list('ABC'))
df.cumsum().plot()
plt.show()

# 7. random dots in a scatter
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sizes = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.show()

# 8. load csv file and show multiple chart types
df = pd.read_csv('Fremont_weather.txt')
print(df)
plt.bar(df['month'], df['record_high'], color='r')
plt.bar(df['month'], df['record_low'], color='c')
plt.plot(df['month'], df['avg_high'], color='k')
plt.plot(df['month'], df['avg_low'], color='b')
plt.legend()   # or plt.figlegend for legend outside the plot area
plt.show() 

# 9. subplots
fig = plt.figure()
fig.suptitle('My SubPlots')
fig.add_subplot(221)   #top left
plt.plot([np.log(n) for n in range(1,10)])
fig.add_subplot(222, facecolor='y')   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

fig, plots = plt.subplots(2, sharex=True)
fig.suptitle('Sharing X axis')
x = range(0,200,5)
y = [n**0.8 for n in x]
plots[0].plot(x, y, color='r')
plots[1].scatter(x, y)

# 10. save figure to image file
plt.figure(figsize=(4,3), dpi=100)
plt.plot([245, 170, 148, 239, 161, 196, 112, 258])
plt.axis([0, 7, 0, 300])
plt.title('Flight Data')
plt.xlabel('Speed')
# plt.savefig('Flights.png')
plt.show()

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')

import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
df = pd.DataFrame(
	[['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

# 2. read text file into a dataframe
header("2. read text file into a df")
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or last 3 rows of df
header("3. df.head()")
print(df.head())
header("3. df.tail(3)")
print(df.tail(3))

# 4. get data types, index, columns, values
header("4. df.dtypes")
print(df.dtypes)

header("4. df.index")
print(df.index)

header("4. df.columns")
print(df.columns)

header("4. df.values")
print(df.values)

# 5. statistical summary of each column
header("5. df.describe()")
print(df.describe())

# 6. sort records by any column
header("6. df.sort_values('record_high', ascending=False)")
print (df.sort_values('record_high', ascending=False))

# 7. slicing records
header("7. slicing -- df.avg_low")
print(df.avg_low)							# index with single column

header("7. slicing -- df['avg_low']")
print(df['avg_low'])

header("7. slicing -- df[2:4]")				# index with single column
print(df[2:4])								# rows 2 to 3

header("7. slicing -- df[['avg_low','avg_high']]")
print(df[['avg_low','avg_high']])

header("7. slicing -- df.loc[:,['avg_low','avg_high']]")
print(df.loc[:,['avg_low','avg_high']])		# multiple columns: df.loc[from_row:to_row,['column1','column2']]

header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9,['avg_precipitation']])

header("7. df.iloc[3:5,[0,3]]")				# index location can receive range or list of indices
print(df.iloc[3:5,[0,3]])

# 8. filtering
header("8. df[df.avg_precipitation > 1.0]")	# filter on column values
print(df[df.avg_precipitation > 1.0])

header("8. df[df['month'].isin['Jun','Jul','Aug']]")
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan")
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))")
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']")
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# 11. iterate a df
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print (index, row["month"], row["avg_high"])

# 12. write to csv file
df.to_csv('foo.csv')
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)
