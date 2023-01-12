class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s
        maxi = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                st = s[i:j]
                if st == st[::-1]:
                    if len(st) >= len(maxi):
                        maxi = st
        return maxi




#tests for longestPalindrome function

tests = {"a":"a", 'babad': "bab", "cbbd": "bb","bb":"bb","":"","ababababa":"ababababa"}
print(f"\n GOT \t<---->\t WANT\n")
for test in tests:
    print(f" {Solution.longestPalindrome(Solution,test)} \t<---->\t {tests[test]}")

big = "reifadyqgztixemwswtccodfnchcovrmiooffbbijkecuvlvukecutasfxqcqygltrogrdxlrslbnzktlanycgtniprjlospzhhgdrqcwlukbpsrumxguskubokxcmswjnssbkutdhppsdckuckcbwbxpmcmdicfjxaanoxndlfpqwneytatcbyjmimyawevmgirunvmdvxwdjbiqszwhfhjmrpexfwrbzkipxfowcbqjckaotmmgkrbjvhihgwuszdrdiijkgjoljjdubcbowvxslctleblfmdzmvdkqdxtiylabrwaccikkpnpsgcotxoggdydqnuogmxttcycjorzrtwtcchxrbbknfmxnonbhgbjjypqhbftceduxgrnaswtbytrhuiqnxkivevhprcvhggugrmmxolvfzwadlnzdwbtqbaveoongezoymdrhywxcxvggsewsxckucmncbrljskgsgtehortuvbtrsfisyewchxlmxqccoplhlzwutoqoctgfnrzhqctxaqacmirrqdwsbdpqttmyrmxxawgtjzqjgffqwlxqxwxrkgtzqkgdulbxmfcvxcwoswystiyittdjaqvaijwscqobqlhskhvoktksvmguzfankdigqlegrxxqpoitdtykfltohnzrcgmlnhddcfmawiriiiblwrttveedkxzzagdzpwvriuctvtrvdpqzcdnrkgcnpwjlraaaaskgguxzljktqvzzmruqqslutiipladbcxdwxhmvevsjrdkhdpxcyjkidkoznuagshnvccnkyeflpyjzlcbmhbytxnfzcrnmkyknbmtzwtaceajmnuyjblmdlbjdjxctvqcoqkbaszvrqvjgzdqpvmucerumskjrwhywjkwgligkectzboqbanrsvynxscpxqxtqhthdytfvhzjdcxgckvgfbldsfzxqdozxicrwqyprgnadfxsionkzzegmeynye"
big2 = "wgjtmwgpfnoeisdozatlhfvcqzlsffkoxrsdjhryqtppdeqrkjabodgtmkthwmtmerxlazsfdogsrwtswhbqclpcagfjlfuyvsnummfjmmxpdhupwkztnwcbppbbwfnwfaoazmautdiutzkwfqibglhypfamgxzsfctapkjimmyazulehprmzfvhaxzbobhvsbxscimjnmibivwbenfrhsudmpmkkbphjyrgjficjvfosrnhdsnjqtaycmyorpujyloozeeinqfsesuauqmsxmoafoszqrzbgechluecfdxulmcxxbiqvqkohlgqlqxierzbyradeoebbdhyjdkiaezfphfetiyelelunryvmczewjwkfrgjvdbouorqymmamkonncostamlpyrxoxnccbilnqdqbeieqncitfgitluvzxildtsiaipbskicepbvhtfdgxfiyywznzdstzvayjmwvlolhtvpekyakajeixdjkbbdlttldbbkjdxiejakaykepvthlolvwmjyavztsdznzwyyifxgdfthvbpeciksbpiaistdlixzvultigfticnqeiebqdqnlibccnxoxryplmatsocnnokmammyqrouobdvjgrfkwjwezcmvyrnuleleyitefhpfzeaikdjyhdbbeoedarybzreixqlqglhokqvqibxxcmluxdfceulhcegbzrqzsofaomxsmquausesfqnieezoolyjuproymcyatqjnsdhnrsofvjcifjgryjhpbkkmpmdushrfnebwvibimnjmicsxbsvhbobzxahvfzmrpheluzaymmijkpatcfszxgmafpyhlgbiqfwkztuidtuamzaoafwnfwbbppbcwntzkwpuhdpxmmjfmmunsvyufljfgacplcqbhwstwrsgodfszalxremtmwhtkmtgdobajkrqedpptqyrhjdsrxokffslzqcvfhltazodsieonfpgwmtjgw"
print(f" {Solution.longestPalindrome(Solution,big)} \t<---->\t eynye")

if Solution.longestPalindrome(Solution,big2) == big2:
    print("big2 worked")