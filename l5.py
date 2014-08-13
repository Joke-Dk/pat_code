str01 = list(raw_input())
sum01 = 0
dic={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
for ch in str01:
	sum01 += int(ch)
#solve the sum01-string
ret = ''
sum01 = list(str(sum01))
for ch in sum01:
	ret += dic[ch] + ' '
print ret.strip()
