NO_OF_CHARS = 256
  
def bad_char_heuristic(string, size, badchar):
    for i in range(NO_OF_CHARS):
        badchar.append(-1)
    for i in range(size):
        badchar[ord(string[i])] = i
  
def search(txt, pat):
    m = len(pat)
    n = len(txt)
    badchar = []
    bad_char_heuristic(pat, m, badchar)
    s = 0
    while (s <= (n - m)):
        j = m - 1
        while (j >= 0 and pat[j] == txt[s + j]):
            j -= 1
        if (j < 0):
            print("pattern occurs at shift =", s)
            s += (s + m < n) and (m - badchar[ord(txt[s + m])]) or 1
        else:
            s += max(1, j - badchar[ord(txt[s + j])])
  
# Driver code
if __name__ == "__main__":
    txt = "ABAAABCDAAABDCBBBBAAA"
    pat = "DCB"
    search(txt, pat)
