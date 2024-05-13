###Noise Injection
##Randomly choose an item (negative sample) not included in the original item sequence. Inject the negative sample into a random position in the sequence
def aug_edaNI(seq, itemList):
  ##seq: item viewed in sequence
  ##n: the number of times the process has to be repeated
  ##itemList: danh sách unique các item - tương ứng với negative sample
  ##List ra các item có trong seq này, thay thế random 1 item trong chuỗi bằng 1 random bất kì trong item này nhưng không phải là chính nó.

  #convert string to list
  def stringToListConvert(string):
    li = list(string.split(","))
    return li
  #convert string to list
  seqList = stringToListConvert(seq)

  randomIndex = random.choice(range(len(seqList)))
  #replace an item in seqCopy by an item in itemList
  itemReplace = random.choice(itemList)
  while itemReplace != seqList[randomIndex]:
    seqList[randomIndex] = itemReplace
  else:
    itemReplace = random.choice(itemList)

  ##convert seq list to string
  seqList = list(map(str, seqList))
  seqString = ','.join(seqList)
  return seqString

## Create new dataset
def buildAugDatasetRS(dataTrain, nAug, fraction, augMethod, itemList):
  #get fraction of dataset for augmentation: fraction*dataset for augmentation, the rest is remain
  ##dataFrac= dataTrain.sample(frac=fraction)
  leftFrac, rightFrac = train_test_split(dataTrain, random_state = 104, test_size = fraction, shuffle = True)
  #with every session in split_dataTrain -> Generate (N_aug-1) more session like that with one item swap/ random in aug strategy
  rightFracLen = len(rightFrac.index)
  ##print('check n',rightFracLen)
  for i in range (rightFracLen):
    currentRow = rightFrac.iloc[i]
    ##print('check currentRow', currentRow)
    for j in range (nAug-1):
      duplicateRow = currentRow.copy()
      duplicateRow['sequence_item_ids'] = augMethod(duplicateRow['sequence_item_ids'], itemList)
      ##add row to rightFrac
      rightFrac = pd.concat([rightFrac, duplicateRow.to_frame().T], ignore_index=True)
      ##print('check rightFrac', rightFrac)

  #check again
  #after augment the fraction*dataset, boost the number of input dataset => combine with the rest
  dataAug = pd.concat([rightFrac, leftFrac], ignore_index = True, sort = False)

  return dataAug

####Redundancy Injection
##Randomly choose an item (positive item) from the original item sequence. Inject the positive sample into a random position in the sequence
def aug_edaRI(seq):
  ##seq: item viewed in sequence
  ##n: the number of times the process has to be repeated
  ##List ra các item có trong seq này, thay thế random 1 item trong chuỗi bằng 1 random bất kì trong item này nhưng không phải là chính nó.
  ##convert string to list
  def stringToListConvert(string):
    li = list(string.split(","))
    return li

  seqList = stringToListConvert(seq)

  seqCopy = seqList.copy()
  n = len(seqCopy)
  randomIndex = random.randint(0,n-1)
  ##potential list remove item in with index random
  seqCopy.remove(seqCopy[randomIndex])
  ##replace an item in seqCopy by an item in potential list
  itemReplace = random.choice(seqCopy)
  seqList[randomIndex] = itemReplace
  ##convert seq list to string
  seqString = ','.join(seqList)
  return seqString

####Random Swap
#Swap random 2 items in a sequences
def swap_item(seq):
  #convert string to list
  def stringToListConvert(string):
    li = list(string.split(","))
    return li
  #convert string to list
  seqList = stringToListConvert(seq)

  random_idx_1 = random.randint(0, len(seqList)-1)
  random_idx_2 = random_idx_1
  counter = 0

  while random_idx_2 == random_idx_1:
    random_idx_2 = random.randint(0, len(seqList)-1)
    counter += 1
    if counter > 3:
      return seq
  seqList[random_idx_1], seqList[random_idx_2] = seqList[random_idx_2], seqList[random_idx_1]

  ##convert seq list to string
  seqString = ','.join(seqList)
  return seqString

####
def random_deletion(seq):
  #convert string to list
  def stringToListConvert(string):
    li = list(string.split(","))
    return li
  #convert string to list
  seqList = stringToListConvert(seq)

	#if there's only one-two word, don't detele:
  if len(seqList) < 3:
    pass

	#randomly delete words with prob p
  rand_ind = random.randint(0, len(seqList)-1)
  seqList.remove(seqList[rand_ind])

  ##convert seq list to string
  seqString = ','.join(seqList)

  return seqList