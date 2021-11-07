# 5919. Vowels of All Substrings
# User Accepted:918
# User Tried:1129
# Total Accepted:923
# Total Submissions:1413
# Difficulty:Medium
# Given a string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', and 'u') in every substring of word.
#
# A substring is a contiguous (non-empty) sequence of characters within a string.
#
# Note: Due to the large constraints, the answer may not fit in a signed 32-bit integer. Please be careful during the calculations.
#
#
#
# Example 1:
#
# Input: word = "aba"
# Output: 6
# Explanation:
# All possible substrings are: "a", "ab", "aba", "b", "ba", and "a".
# - "b" has 0 vowels in it
# - "a", "ab", "ba", and "a" have 1 vowel each
# - "aba" has 2 vowels in it
# Hence, the total sum of vowels = 0 + 1 + 1 + 1 + 1 + 2 = 6.
# Example 2:
#
# Input: word = "abc"
# Output: 3
# Explanation:
# All possible substrings are: "a", "ab", "abc", "b", "bc", and "c".
# - "a", "ab", and "abc" have 1 vowel each
# - "b", "bc", and "c" have 0 vowels each
# Hence, the total sum of vowels = 1 + 1 + 1 + 0 + 0 + 0 = 3.
# Example 3:
#
# Input: word = "ltcd"
# Output: 0
# Explanation: There are no vowels in any substring of "ltcd".
# Example 4:
#
# Input: word = "noosabasboosa"
# Output: 237
# Explanation: There are a total of 237 vowels in all the substrings.
#
#
# Constraints:
#
# 1 <= word.length <= 105
# word consists of lowercase English letters.
# keywords: feature extraction; counting cases
# O(n) Solution: https://www.tutorialspoint.com/count-the-number-of-vowels-occurring-in-all-the-substrings-of-given-string-in-cplusplus


import collections
import itertools

V = ("a", "e", "i", "o", "u")

test_cases = (
    "aba",
    "noosabasboosa",
    "nsezukxxfizmsyklbnapslntyoxcqringkizyfwrkzlnrnlngpfbrnvjgarsnsnwpcypisjzwdulvywhamnilpsxnikkobaozgptrxsdavgnixjillcvrayliscjizartkfsfdmukxxctslolfezijrysjpqxgatdkhoggxqifewcuctgwviudzjwigbjacreernsoampabfnysygtxzkgkgxopgajgxdzjicwtvacqvrxndlqyzothxkwmhaxljbjrnybgjlllcxwzuzagpamznwtjdwxsyxooamybmcmurafztbapmqvhdbfbutuqqwhphwhpaddikphtztrttpjrffzydanseiueeboywpmifxbbytipxtgmmxpvbsvlwhodqzfqjqgywlgkkpedsypqtcxzncxknwqlbranuizejweoiesutcbteisociddiukjyobxpucmgyayythrpgwalljklfjtigedzgxntxnrmsbkugjtkpuxyxfiyctaucbpkjkjiwcwegqonqivauvchbfeyqqxkzvojphogqrnjnmsxnikjwktoyppoubttoljwvdcgahjbxgdlhcafpomugaivakyazwtqfmrymbijbisoncqthfrftgjqdzrxllnbxajqnwyleloohwidiphhoscagvxmskvfrrnbgjbcjaljcxyuxzgbanlltcqnvbyjdmclqrcjjylshjvvvhhxckipbyglfobhfgldtwdapzjberhcsnphfmdopruonmduyrpyiagufgqdtbiswbfymexqgakdlpaybplicrgczhtbfgxwktxebrpybkrtohaheupiupsshrevvwyrtygnwlogdrwqqzonvifgacejcrdgzhyhqqrpmnptxnqkplnsiyovgmrurlausdbxaabmkpmjvpiambnskgqwztithfimhwchkhfjsrfplcquuudsnwjaqfawrvlolljhvwakxzduhgbebmkenrbwqevdhlfilnkwdcpszesndxolzkuktkscsllyyznpumobduznxahsbxqycbjgsgiwyvtklbsfvdbkxeqfmhtxqhmhrmwbaowjqdjlcvmxhbtmzbyjsrvnmtgjpxgklqwatsptkkasidwnhgrmiikbkecmfornqmavpfrzofbmbrpcoqkfytabmofeunbkfenzdcjsdifogdbdqlmvemysardeqtkzmkorsfyyrwdnwzzbegvvisgyysxcymhwhjuknndaitdmpvunjqyixbvlppxwdthxdaoncgcerwlppbutidftdtkgdzsenesdjygemzcoeodzjmdqbfgklceraliklwxjkmlbhmdipniockgvoapygigckodzqzvnwdwkleizczmzxhymmhinyqhmsdvtovngmyiijcuclgmkjixcclgvgqqzuoqkpfydldnfszyukorxelckvhsxzpjpdkjjhbqjytaboiokyusruatgletshahrojebgtzdarnxysokrziozjzvxquqyoyuooeaqhlnfitrhzkzdfxcdsgghhuulsechzqetuasrzzkyncrmyjoivzlrtjmrhbymrfpjgpryxzaszzlscvijasodwikwfkmoswxozhtwydqxulxjrkehjjxofzkciefrqjnvktnmcdgnggoaxeyzneavaqosdulixypszajupzbcchpblndcaxsftdotxlfspvenbriecngbexicuskjvbeyuxmxavzsuylpigppxqrzghuwsdaqblcvwosyvjfpeemuuzpcjqfzkwrjuzjopztgfateppxlptvonnhunlorgnleagjhrdktrrhdzvdxuhestapdnhcmjblqfwupdoryqksniagolbohjbhxwbomiqlneovwacvtfuhammbbcbriqtqfliemykgxgwulqdnscnagurwkpxgpzrushqzdqxehcykambiquakuobglljxailhawagtuztcocrdgafdnnvyqwfvpzdttibnsircuyhzscmazdpnrxqiihyseckuuscfqdestyxyjificmkuipnesvzceldbkonnrkxafukfitojfonkrvwkcyqsgbsfdrfgndtkrtthccaowdgjfhwqzfpgoezvoclafmkimldrbzmmpfyhayeihenlgnolenjtobuochionknyqtkjprramkiecykygceyabjyzbqiyjrwhcixaxjwzdhqiutgghareewnvuqahitbclbsqxnpskfmdnbtndkuzjhzwczojfrjzdapvgbaajksavywbefdnfhzezttuarnolgwnngenowfgfunrktkzokkikfanmzxdjitzmcdwzsouvxbwasinwcyjfjazhnsjrqomjrvsssjjfiuvylylyxrhapitoqqfxnvpjbbutpalkpjmazapijoqygducnnpvijlraangsonwfbsecwxsnjwabpbhdallslnrrgbkeugbsesifbqcsezibxzcplikejmdxnqwahoixkxyrgdwldvrsdtcfnxqjmrcpmqglwyzgovrjdbnjfwnfgcwibttwchttpnnffgfktjbasoovtdyyrvqojlktcythiiknfkujdpdviebdkvpyvrgjplnykmwyoawspdcyhsxnimsufmdkpqyftzongmrqqbhmpviudpgcnarksiinurujqtilhzfairthkknkthkjdoalcdyogdhjuceyrnwweftwjonduknxvlzfsqgixnshgsvfhsxkmfgqhioiurtpyqnyndrghsxyfpyipsocwchxokkmdjhefzrdajgfozvekaqffyavhtmaefyurozcbnewxtodncsxnxqsbmhcmczussaoufvihsqqymxmndefgmzkqvdxckmfiwuqxlukdwawwnqmwiystjwudifeobnkoknjufejicwrnsuwjqbkjcmvnitmfqghueoyblmckxlgtyggyenwrpprqxummkrntomyhpjksqwvguqvkqnmflrscvwdpiwtvqiwbvugqdszvzvizyvljfiafzctnydmwlnjibeoedqnbfvwbxgulhuonegotkgsegnrmagkqcgaenhjhdatxschbpqpztjvgguqpbtfgytjdoplodbrhcvomicgehzffjvvacpvturbwjbufjwzmmmyghrfeetkpgfhoakttfcixzkaipcfwcshmqbqbcvdvmlmwjsdxyzeabobrubrymqgqaocdxmgpzatxxjkudecwxaxfakkengowpcdqwtktadhddbuoxymecwlcdghvvvelfqawzkrkiinijnmjckbohbwiwufhigdoexxxjjnnuqxqyveybmvmokyantahfqrsjwjfvxiwxepkyylxdreezbqbewpqqppygumxeyiykdjhuwyxpejyvrposbqkjhpujfjhcsddtddsucovlqbetwulnsladlsnmyllsgqunlfdqziqpyefngcczqxcjimgwdrxqfuegzxcnkkdunlbtgwgjodejzucpriucdxmhfrjcvtyoxgqpbzwspdtqpkpwvuqbjiungwofjcejamupervujtnttjzdwlzidbubxlklpisioqkntafxywufdkevtigttzjindfgihbviuqluevhdzcjobungncfrcqvwseyvakmhhsjfzgmkfcbylbjyfjutescycpjrtmqbgcgvrmnminygxjxeavfwqlosnvsgqugtcdqwkcuyuhsissowvqkjrizbylhdtkxszhzbpyabnhtyubcmocxjpwfxaigmwiqonmahndrxpdxjldioxjpoymocrczvxqbquwbvhtvzlpmydbkbnbwrsysbfeyfqtfbujhixcvqohzewstvbhqxcxfsmwyrlcvvajqdghvabnvtkzeiujwsmvjrihwytmefpqvffgyyhitgewkjgapripytxjnlwgockjxrmsidxovkrzsmtonidhealqgsnfbnyxekpushoinxdubasulmoajeginofnicxeoeifnkoobfduakmwtslgqdmdykknmtemrthydkbklmlkqaecivitbtloclydspwkvwceftlswytmoaicrmyjovfizklwsndnchcltcocxmxyjcbgscrxvnimriekfljbeuerjhihlladoggxzjjqhbmaeyjnrhfyptdrlmrfafumjylvbgystphsaczikvrbvcehzglopkwqmljuqyhpcjioekehhrkdtewwkhdlewpckffkjqgwvojfaukqsuewjtpqlevscephujbtjgiwfwvrsavhakorbqdsxknayodflaoufhpulhdzcvmuzaipoljhnfdboqxercxagcigtyvpdchcyxjteorlvmawrzwdxhuxfdplhvqxbjjrzlgfljhgvqnltyyrohligqqlnqzzkpiypjhqlbbhvmdaknrgvrvxptriqxkfugggifkhgqmuppkegatyaukdfcqilxgnhybipmhtumqgcmvbopblzkphncpxnkcjzkqrghnsichaqmzyivqfmjxbbexrjvxjcdutrpjcbefpchctgndhltpslvdbawjvyayajnccwqawuqhdnlqdavtxycejucskyqpxifvcoahvmbiqbiluvstrvlqzdyvbprqchqsejmvwszljroahuqlsngecakouztvraowdxxinfycvybirfojqsdcedgfsotduipfzcotnetfiuzrponrlxsrjzsijxttxqegbeufqkfyqngamrllixqtgxxwdzwvqvfyohlajzymghjkinigfdvhvncjviufwlkjbkmmingfvtwsuizlfihawbbrzsimpputsuccppbhzhfddunpcmwsrcfobabjvqxytvswqowofjattomvumortqceyqltrtvnoibhusymyddxkdjowbgdiupotqktyxwmzaungijrncjxlsztkgfrotyljmuofdossrztzprvzwntocfkbmllrdpmnmbakqxowkgsimceapeqlslrwvkkbrdikfzisnxuwsjecqjrwqmhezratdnwnwagcmckhpqvlqqtpteqqqpthjyiwsirirovjeubjgmvnmkzyekjsdxngdngpnzygtksmxfrivisnptcbdffiwynummdlpvvwiunpjlncisysbllkzgsjhtiihmsyrhcxmgxmbagamfpnbmcaudzwaoekyvbrsrxgrafqyorsmdhpujmusqcfmvafzvwmsmpjzirgvtpzxjiqcspbgzftyaigbgdnhcavxvhpnzfmsbxvcgpsbqfkessbrxbugmwfxmutbbuhclyoyomjusqenxthhhucbnibaozsfbotwuggvawnvienrdbuzusmrengwbytisgcgmyqgqpbjkkqhxtpyzsqthedrekqvytbnbfumagbinsjcqcglikbkztayzqpsypdsmmxgltrlarlckdcrkwxloavcqowkxhvsugevagrkjofjvbrkzqbuxealkfprijzfkazplvrkzhhzhkkmbiloajpxvtpfhpqzszphmfmkqaunpihwvacqvhmqfuoukpxugblambuebrrqjfrmzckijyokpjvvomsjisijjcxixichdrusmdouoshlyjhimdizsgmepvdbqyomumyotabkinpseisnyksgfkoypmkekpevbdgfrrzseejcdotcmwyivfbhizotsbhzsbricnwhovdbjjkhzabeagatcikzdaszlcjtqneppuvsdfnzcvstbrzxhsjpkslovkhgcwxdpdzbztxbqtwhjqqnmbqcmuwiwbtlnsjvvccsootvteiauejvxsmtkfawsmqounjrvimhtmzkhgmfsokdsdwlknweulxzpmnbicmvzwxyfkprlngldmeynmegvroysjelxlqshqibhxmrmdkgvealqgwlvuryuzeghghyjwsgrfjmemduzbnmgoturzjdfrjrzxgeqymkuskdjhzymxhbfnbpsnoomrifittejmwtgvyrbwjkywtokfmnkigiskwaeybtctysfgjxaauailphzbzawoborceztbvicswsukjrjwdnzyigxhtdmqpdidhftsjogftnpzfnfpjfpluutsnucrzqeewbjinbxqisuhtxxlxbssbwfvzwfvvbkhlaisoonyeffsjaubksaxvmwfwhnvgloqlcjrqujkaflhjtqkrhmgftqqivtxmbmloxbgyyjqnyohdockbaajyetjyvnsnbuuntfzrfradjjdazdybvupovjtbsoegwwxopohzhiyjwmacjsnbxkohrtaspadpjcguxouucdztefirwpjommteizibejifpsecddjtvsdiufldowiceajdgkfxwxckshwdfgmvjbdidezjkzswpjaqhabwuhbspykbqqrlcsnigxppyjgammuxvhrpzbgtmdmxdbbtldhmhgfnppudwibhorhrijzynfjlntfyekatvvvzkspmxbzuznjklypgrroksbtxmzrwvlguxjncodploerwpvtxkxymqljopsyxfolqzrujfwngfameyywhfwmnaljquoiijrrkmjnibkzhjyjmowizununoizzywbfkyftvuwxqtvolhccnaxfjyskxigcpjsfmhaskrklvhmseubroaybbdfhjwhzlmgbptwpdhwgpgjdqoswqzzykhimsqrkjrxuqfqbkyajlgwssnxrefquupsmxquzzjtiiemahzajbbqralnmtpfjmeqlkdmqhxlrpkhellihilpahlhrawmbzytetppydayrorjdzixguigspsullvqdrsruhapvdniqrjflzxeqvknekpszhifbylltyfdoupvzgnxumxxgzgnplbgpzcofvmpzrnumbyoweonxdowdyyednatwpwqnkjswrucfwntboaldlvmcnunvwszjxwgisilgfvjwwqgsqspqxlcbxecmtdytzmijtvqdybdtlukbfwgqpldaqkrbzkscjuidkgoxopioxlzrjqxrvnmchzqetvwczycljrisqaiuxzhkrwxqzetyvwefwvmfjaqtgsniedciamfxalbynpvodmyvckcyqycmqgnmbgfdkneiwxwudnlkzcdbprhpkrckvkxwfmymstprilkvdiuxlbtvhbsbzrpmseeeujrkvwvagiifdrkzlaysxveikwysdmdtkrjqfqxjfctbbflgotduhjftzkehypatwlwtwfmoxfldsvjxegxsunihagfuhygijlzbxpviljmwdtwdshjjwvhscdnnvdgcmlismwhmlqnyhqvbhpcupgztlxwvqxuafxfmjatsbeeytjkflwvwxsnnddzzclgltnloewenyqgurcwywkzyxcbrseatcfwxdaaanflbkxpbstqjtuvskegwcbydhvnagafdbgpksjwjqmigupddgppykwzhvfmcqearhakgubwlxofoltqdpmoftzvhjajwosbmyeruaalubiuymrgfccewwssejrkivxdneizgtjdnngqhnulgpdkmnmgdqojihxlmudkzfmtawrxcyvcsruxqhgfoggucotispysmovjvwuehvmfvkvibfwfeurpxlipkkadyqrjhecujhesbxyvwzidwizrigyxzibifovlpkypaapmtjfdnlszaevnofakztggsmejiszdlebnyiuerikoghtfclorhwjqubohfimwggucignvqgqkbfmovlwypmbptozsrewkweowbwdtgoefpputijbsytizhfviohygookicugaofzcynmpnhhrhwpxyhrdiqfymzfwabqxuqvtnovdpjrrfyrxslvwvltmzkahywccagfznvctqvtjydjetyscatgbczlhhicksqzvfgdjfvbwctbffioezuvmdsyyhjkqfsppsxnpviizpxgeuwqyxqmzuxjjwmnqduarvurrplorxgwytrhqqhcsqlkmljjvnicmpuuahoygtgvofslelwctcpgzznnpojvtpodqkuaqdfbhnozeetrvbgtjhdlwnnxovzblojiuroqrmddhsdmubpxsrluzeiniwmjepsdyukgqnfrbafsdviwshceqwcnznrhjqgbejlobrfvykvbuahjjatguzybreejxbqttiyamexqueuclxamhrkpdknxtattbamkmxcnxxynttqiwjqbqlylryfapfpcqikmmajajyihzyjenyxkixwutlfietkfppntcbihfdushuiyusqcgwezproawghyoohyjvxkjipiepoqmuwszjsltgjkctsvsyqsznmtyffisgbqhkasmcqqtnoxwubyjtrgvehidkozfeiriwpnrtxgvyjnegpzywahnnftynhgmcnamsuebgebcuoalnpcnhptehopecwulhrxlzdxvgbpkdesvvdgyntkcvqgehwumxfrphndjitiokbtxznbvgwqvkpxjqkjimvpwduobamyxpendsqhtqgsqkphmypgyioiageuuhvqdaysnliljbtcqostpismsnzlvnpcaf",
)

"""
def substrs(word):
    return (word[x:y] for x, y in \
               itertools.combinations(range(len(word) + 1), r = 2))

def count_vowel(word):
    return len([c for c in word if c in V])    
"""


class Solution:
    def countVowels(self, word: str) -> int:
        cnt = 0
        # count the substrings containing this character
        substr_cnt = []
        for i, _ in enumerate(word):
            if i == 0:
                substr_cnt.append(len(word))
            else:
                after_cnt = len(word) - i  # b, ba
                before_cnt = (
                    substr_cnt[i - 1] - i
                )  # [a ab aba] - [a] = [ab, aba]: substract substrings dont have word[i]
                substr_cnt.append(after_cnt + before_cnt)  # [ab, aba] + [b, ba] = 4
        for i, c in enumerate(word):
            if c in V:
                cnt += substr_cnt[i]
        return cnt


sol = Solution()
for tc in test_cases:
    print(sol.countVowels(tc))
