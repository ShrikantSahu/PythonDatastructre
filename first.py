import csv
import re
def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                return data

def create_list(data1):
    x = []
    for a in data1:
        if a != '***************************************************************************************************************************\n':
            x.append(a)
        else:
            continue
    return x

# def create_csv(data):

#     with open('export2.csv', 'w') as file:
#         writer = csv.writer(file)
#         for a in data:
#             writer.writerow([a])

        

       

        



            

       
    



#data = file_read('contact-id.csv')
#y = create_list(data)
#print(y)


b = "BYJKTGJFIFVMRPFNFKATRQFORMGKTQCLZTNBWNSORUVBPKGJVSRMQAATCYZGGTTOJOZNXDYWKEJWUAHJKDJWBAPOYUVFKEMYWNBJXCCYIYLLLTAUNJTPMJJEPWOPNXLRQUKHDMEUKWUMSBLTFFYHMCGYYMHOMJDTNAVYDINWSDWBSNGIURHILNWRXSEAIKEFAUEFNHQIRESGQSSAGBOWCGUVWHKJXHUDIXVXRHOUKHUXUNDCSNRZYFDEAUYBWHNKVBLMRZZBDMDZEXPSLRUFFKMPHVQDDPDOYTKLHIVMKJVKGFCEKXCJQZXOZYAWRABDNYKUQYTXNRRVWWSLFOZCAOVZVMYMDTJTFJQCLJAUUADSBCPHMPVTIPWNQNUPOZPNATMJAQXEKCBACJNWETOTBZRHOBBGGQFWOKCMJYMZSHJCACSLSINKJJMUOERKUHBDISFXJTZDMJLFVZJIPBVACVEZTJXHIQPALEYYOVXGHQENCWCQPSDSTRQBGCYNCWANBEJIDBXFJVONTTPIIYYSVLNEHELAEIXYNWRVNYRWYYZABAKEPPBGECOHAJAJZKMKLSDJCEEOJFRYCUEARWPJGMISBAETOHUITGGFSXSDHZMAGIEUNQEZWVOTCFMSCHTYVABKONCBWQLVYCEDEEAGMORVYEIXSHEXAIDVFDTSLFSHSMHPQNWOQBNNIBNEXPNYPXHUFDERDNVPNRCFJCZTDKUOZOSTPCFIPMXCUVXHENXFKRVUVCJKLLEGXRXWRVJLCXHSSNKIMRDIYMOIKHHXGWZXRSCXPBVODPDVQRLKTZITKDDADTLVYCAYZIFOYRMMBIVWOZJXKYHRVHUWKIZWALJINMWUXHALRGPTLHZIDUAFSTNZEABAUMWGQBNXXBMNRBQROERUDHUFXCLKCQKNYTBWDTLAAPRWCCVQKDHXBCYSTUGVCEQEEZRZETWJDBFPIFSQNCICXEDWCIQTZUENUTHVNZVTBIZUROSAMTBWGCTYGNEJIVQIKPPTVXTXUBDKCGDYIQTPVWGIFBMFEUWRUOFWVNFEDDXAPFXCULGZXSBIPPGMFXTLORMJQJIRFFLNQJLLEOQXDFXWOXKOYTBYFTHEWLFMLFCPKJCBIXDEXGJSACSLNWYVDGMOFPHLTQRDEMJWSPXQTNNOOIVRXQLITSCATSAGNRXJFQHEORNSGMKKDDCAZKWLLZURYNVNVRSQJFVEAWKVTBMYDBSNRFDDGPDEUOJHMQLZYBYCOJDQYFVYCTERCUBJYEDCDWFNRLPVZRTZOFHGXOCDRQWEIJTEQYHJJKUCODSMLOXRVZNJPMTYDUZLQHWVPLGERREIRYFCOWXLJRDXLHFTZFAWUACTGDQNCQJPGTEBIGUFBZTKXHYJCVOEHCYRJVLMPVTMGPNWJHXVFZGRNJBFECVQTAFSCRILSKLQXAVWFZDAXGVRQXPBNLKUZORTXLIEDVNXVBYPRDZBKYHAYCWZDIDBGPSYWHQNPOLKPNBBEJQISDLHGXTZYTDQCCMMNRSCLBUXZVSDGXROLFUFVRXLSJRPIJIIJCTSKYADAVWKKGGPCWYBXAQRCGRQHGEAEFOCYEKXFJJKFEHTZVSSMUSRCOSXJVJUYHXKEZVUJDXITFOISVFZQZOOXBPEHZYHBTBCGVVQYBSAHRNSDCTOXMETEXCFZOWPRHFYDVPFXBVVKIZTSYAVRDYHQYXDHLERGHOQSTYHOUGIMGPRPSKDKOFSGGZUCKHWUAEBIRCVDQFERTXGEWRKFEMBFVXFGKUUMYEMDWIIZNMTMQQVHRVMSDBGWJFUWNTXSZXGSOIVRYHKETMKTCEHKVRWRTRNILZSKIJARXKLYYTOUURWGXOAIADQSAIMCGHWPYPTPCQQBOUYBZJONXINCCDLKGSUDRZHRHZGJUGWOACMXFMWAMUWJQMCSDCZLGMQUFWCUFOUSYPOEFEFUGGWDMFVPVPOMCANKRZTLENNKAQCVLPPMYHUDYSXHBHGWGVNPQVHZEYNVICBPCXULJMUZQWXMISMQQLEJUEVISOSYKMCKOHCIPVBKMSVAECGMTPPSSKZJFVBEZJRHXLFGYAERYCYZLBVWILFQYCPCCBBNMULRSJHEHSUGXBYUHIOJEBKWUSSYKYZJXYMMWKHAMPRTOZHFEYRMZMJCCEIBCYMKFDSRWVQVKDILCGKDANXIGMLZUEXQMNWNPAWWAVIDMBIDQRRNTODNMUCGDHEOSJYFOSUNIHKLOOXRWFIMLDPNELGDRGEYUGAOCBLIDZSWDCYBNVLEQLYAKXQZIKFROPEWZQAFFVKROCOGZJGOSIWAMDBIRENZOXEIMLWJZPFYWFISVEBPLGSUGYLEJIZBCCSLDDHFLICGXUOTYRHHNOFMQSFLJAGVGGEZFODFYCCRRHCTQGPLRKGKXRABFYQAIIXUIHBTMRKCRKINDCQEGEQTLQUYZMSTVSCHIAZGTQRVOBVCNJNVGDCMWYMNEBQTCBUUHUNYPMTONLXVTGPSMJVPHJAFOMDUSOFSXGNCPESLKSNRQBEBVBGUHNDCCNIFCPRZCLSUVAWPNCWJBPLBRMNJKSOVEUXXTRUEPZCLJGUETFKRYSZELKHBYIOGFARYLQEHXKQBLDSUBWWGIDHDOHQWDFOJPXDEFTRMEHSSHJBQSAJXQNTZLDMMEFTGABFDJFOAWUCPNTEMEEKCLCBVAXLRNRHXQISTWKEBXPFNVTBTLQOMUBYCDSIHPEYCSVHIAYPUDWCCAJNBJHZPXAEVRELJUVGLHGPHVBIGXSRNECIIANHAKCBYKWWXBOYVCGYZGGULTQBGVUSXXGUMAYKIDTZSLVJMZINNKZAKVXUVHOGTEHQJZVSNGQPGFQWJIZKUVDVSNHXKGRNTAKFPYRLEZEAWDAUGDHFNOEDQUQCGTJJBMOMPGEXWUURXMKNDAYSCPYOJUZQKNVXYBUXGGGKEJCTQYGMJZCWKSRHCWQRLEPOGERNFDYYZEVSGJJOXBDBKTMQJCSMUHMEKDBNFRTTOEZHWAYTQRMZPGCDPMCRPWCGUBQQTPOZOTAINNHQNTSIKJBERNOZZKQFJORWOAVWMHKHBMBXDWGMVYGQAFVEPKINHYWQJYBMBYWILSVGQSBQZLIHNHKNVIOOIWXZIDBBOWGGTJIBOZYDMOFYLLCXKVUOYTAGRFOKMYRYODATNPRLTCXZGOAVVBLCLYQDRLECGBZQHBKKZHYKNHASCEGUYKAAKDYQERLTWAWCZZPUNKILCEVPLQLWOZJIXSSBUIZFLOMKLRBNWXKTUYWIJLAGUFWBHTAUZVMUNQLGZBAZAOQCAWPTYKRWDDCFQQKSYVSNJLIUMRTHHRTELKTDPUUOZTHNQZRVWHARNGKGJHPHFBALKTQNORHJWNDKIDHDONVLHQKUYUZMZWMBLPTQQDUQFGJMWZDGTKCWDMHXYEMVSRMNXVUTWDCKTZQPSCQFQBXTJOYHZQPHEYRBUDKCPMBELTWSYOQKOQEIJKDSRWIIOXDDVJNMWNQJSUXXEJXDGWDWDPEMQHLHLFKXODZWXTSWSJUYEQDPNCIPYRAMRRSPIPLTJTYUSHCSRMYUMIIUUXLLWTSEKQNCLYAERTTRDSMSOBCALBQVMRCCSQQKHFEQNSQIKOZHGXIVOUIGNHFDUWGACXSQEEMQHTJJHWWMOMPWLAXNCOEFDHJPMXBMHFZHUSFJOUHUHLCCAILHCJFGCBWIGDXVBORSEKKKNRHFGCLBKTRKZMNKLPCURYKHAPZLTZRXEVJODRDCQGWIMYOXEWZJCLXJAXUGCWTZVPUZJYXDVVWAWQZFXLTWJNMSRICCDFDLWEZIDUBIPCZZSIYOHXEQOSLUHSCZOTHMBLYDUZLUICAVKSWQJIPAARWXAWJMPJPUYCZDPHXLZQVOACPHRQUGWTZYDCGSUIMHOPLQWDAWUATOPMLFFYGGXADZFQKGNCQYUFVOCEOOUSBKVXDPXAWWGPGVVFJVTQHLUUNHAGZUPFUNAMTZNDHVNUANSOZLVXJFJQVTRATDFWBTXNKZWWQBATBEAUEFJVNWYWHQVDXVZGOHODBNORWFOCZPWUDBIDHLNHKNEIRTMQEKOSRPCDELEMYPRLWOTAXEPCGVCEKWEVCTEVZZHSMLWOMSWSABINVIFAOSGMXUSGIZZNANGALWAFWYEBLUGERMHDTSSQGYHDSUCYCFELQSOVEQBWPBTAHYRHIXJJIEBSHLHIKTWYRYRNFUPGDNPPULVGKAFCMTXZKRFWNYEAFBFZCHERJAFHGOHHDWUGVPTUBJUBWXNQJFWETPJDKGKKEJGXYVFLCSNQSEYBZKDNRWFEHWOBVUSCVFBQHWSXYCNHEINOJDVPNZTDOJGMFJYHJNJBSCDJHMABWPSCTNQHXRXUOKJGTWJGAYPVWUBDADHWQIHMNTLHVSHTCLCNFLBPCZTGEGKDQITJLWABOWBMGUJBWFRRNYYEHWTLLOXYTACZXSTLMJYEMCIDTNWCISIELSTKKLZKTCNRXKVETECAOZKXBPODFAJCHOADCWJSBWOSWOFTQHTYGBQHBBKZNLWTVOCXCCUKIFTTCUFTNNPAUNHNOFZMRHUFGNFKAUGLQACOCYUWBZPIDYMUKKNXPCURJSSBBDCJKCAKGCVUKUMCKEPLTOVPENEGRIJLKFUBWZETGYFSIAAAYBLOCUTZUIPAJUNKEZFPMKWNOXZDJMYCNOOYDSKINAFBKTANBOCNZFAPNJRLWXNCZHJSLQZOKGVDPZELYJNWVEHHSDUZIZKYVWJJSYLJVRUEWAIFTIEQHLGDLVVMYRMPFEDNSVIEELVLBKRPYLALRGYFNIDZBAFQPZJIAWDXEOKBNUGVDGWILVHCWEFNOVPFSLBZVEMFBTFAFOHBQYODZZWRPXCGNLVQHEHSRBGFVEKWCWYGAKZJNCTUMMDVGJYXXURHZOUFDEHOKFSGLKOAVNCDBVIHMVGPXTINKULXVPQNOFQWZSYYILMPMISSQTQWJHAJXFLZGODGEGZMNCHIANTXODXLMIEDGCWMBDVODTAWYCRIAMHXLFEHJAAVEOHOFWTSLIAYZBXLZFPGKXPADROQSTEPBRODVYUMNNRGSGQWVEKOUJGKVNGJMPOHTCJOXPQUQKYYEAZYXAHNOHCYYSIBCHZMGMXEPDXZNNZGXYMCCFBXJDJBMELFSVMFGXBEKEQJNPXYYPRRTNGVRSYIKNQSNAPGXETNUQMHKUSGMLATOOEXKDTAPOFCRPMOWKKKJVLEIRAIRTZVRBUUYUGAECXXIBISXGTVIQYPFEQYHYWPNRVBHGPQLFXYPHXSVUVBYCXODXLSWKGUGIPJZHCGNLHSAMISXBFMJNAUBBFHQNNTVPWUVHAGGQSQISZEMTGIKOHWDLRFEZWGXGBUOTNTPJSSUKZTYRUUCXWNBLLABWFKJDBZQQSCRTORNLOMUNKMNDJWCQXRUPUMGWXPQKKCVOGFNFTCQYFIAVXEKTNNZKHWSKVVRRYWXUHHEJONPYMVHEJERMSNESSBBMVMLFDSOLDJOCNGBPSYXZSKJPFZOABBPNVVRZALISKTFNTVMRFBCXSVUACTYKPDKQVZCMDEVWRRGZRLQKBFCFVEOZXFTDTCXTJZXRNPSYSYIYJQYJUYHOMIPBIHTYKIEOOATLXXFGZDCBTRNVWTFIYVWRTPUEDIRLOZKZOMVYECIZNPRCTJJBIRCIIFDYCRXGRFPHKERXXREBZPQFHBVHEWFHUXCRZYAYHAAJGDKHNBZFTMRONTTURPRJCGTXRQYUBYPACSDCXIRGISPFVKLEKMZKMMODNXEAUUOYIONJYBQYTQEOSRDFRACUQNQLZSNMNBXMOTBUGOSEQOYUFWONAYSPZQSFTOTJUSNWAERHRRGQWXYVBRHJQKTLHXQMRTBDPRXSOFUMUECMPAECOVNJIQJNOIWBTJIIHXGJDFJFOPIFOTQLDTIYOEYLSHBFGHHIGEHNJFRVYHOJCFGELHQBFVMOVXSFDAZYRHELXGPXFZDOWATTQODPFABKAOQWIBRBGFXLCDQDBJWBHJFSCPRSMDXIHZENNSAPOTPQVGNPPYORXGCJZHNORSFYZOPAVRJSKQNTVSSJCEKUOZLBIRAANSIEAJDLXHMRXTDMYKINNKKDGDBXSRFFLYTYXBABXTBKZQHWWYSWDQTNIIRHMQYGBNMMBZGVUKQZEMBTUFUOLMBOPNIDDSFVQGECGCFJNMQKAYRPLMLLSUZZGFAYPEDEFUYAYBZEDADMQUYCOGDLDTFMIJDQCYCFPPHKWGNZEPCLCGDLOLBUNRZSBVWLBHLIQAYVPIKHMLOPTPOQRGBZOSERRTUMYQDWCNDHQMSONVTRZRBXOGIRRVZPEOZBRAFNACIDKDHUXOPZCBAXOWOOLTPOKXYASLQZHBHVGHMUOUOEOLSZILYYDWOZAXJULFIFFAJUCTLEUQLBVTWPKODKOIQMNFPSKFNWKWAYLNGRITZEKQBXIJRBGWBCJYISISXRNNLHDNVSWMQWZORTZOJICNZZOTZIZRCUMJHXLSYPWUAQKWYOQDVQPFWFYFHMGUOFEKIEZQLYSVLNJMMGDNKEQIJLXMOOMSXHMAEPUGQYJITLIFYOORQARWXLJNBSFXIPWOOKBSTFVSBZZQEQESUIVWCUILKEDARJSADCUFPCIKUORSPHHLPTBTOMSGIFYFONPOQLQNLVHWQFKIDHEUWQJZTTYLMVAJWTAZCJMHWKNFCQJIUSCOWUEPTPETSFOSFEHBGGTPXCAPBPPGUVCEKZSAGAGZKWJPFEQHYTUCTUVZUTMPHAVZAFCKMJZXIPPTDMOIFIBPDLWVMKVEYKQMFQKXPWJQXKQOAOBPFBOXPOETPHQSIXPPXTHWKXRBTWJZARSWFJKGASWSRBPDRCMRDPCROGGVWLDISWUQVHZYNPFQFKDAWNJJLBSDTTJYUQLPULRHIPXVECDBEBZLXHTJFMYOMCFQUWKMQIYKSRJTCRQIEIOVCQJNFOYTHOKNVGVFSDTPACIEUCKWOXRKFIKGNOXFTPDMASLTYGLSWZBUSBQMNWBGQTVXFYBSAYHXFKTALNDTINAUSBGVZHNYADBJFTXAPSXJJPASGBXEGJDZSUKLBRDPDJUSBGQGAWVRGNXNURJUTDPDOUKNLLNLGHGPFLKWRZFDYPVSUGNJHEWIVGJAMUBWPZCYZVMAIONMZMDOXWGYPCDOLMNOOPSAJXORMHCFKYAZKMGBZFGXDIVJMQJLLXHLKIYIOHZJRFDRCLQBLNPFMJWAFBFLGXRAXISKLHYBPRLAUCBSAOUXTFEGCAPKUCEJWOJQJERSGUVNPHDPSASWABUWTLIRWBZLEDCSIMFDSTIXFXREZOIMPQFZOXZJKUQJNKSTURHHGQXVKAZLGAJHGYHWLBHUFNLYTEOLAINWBRCHETQEIULMTHVTHBBGPHWAUGDERKKMGMRYZDFPPCSRDCAMVERJCQLWFFFTFRVJYUNKGHROCLKCPVJNEHAYDYVDCWHLCJWHEPSOEYFCNDGEAGGRPIWEFWAVAITOCDYDKKQPTANDOUEUTNUJHWKTHWAGLNWULFXEICGYNAQKTKKNPRHFEXDZYIBDEIGCSMSRGCXFUIQXICWJRZHJZUINXGYSQQTLBIOBKOAQMVBOKJNRPTAWFXCCIXRQYBUMDPHOZYNTZZMXCHMQJODBTHWQRSPTHPUGXCVBXFVTUGKFRVHOIEQYAHDGEZTEUERWPQFRHBKIXMTJXCRODJAICMABPFOBSGNCSTQJBPWGDWBVNOJGAMOAANSOXRJGAFFUIGETMGLVHFSHRYSSUYVAFEKLLLSBKPHDCJCPQNDPDGWFWNZXQSIRVEYKXOUSWQXAPEEORSYTQVQLCMVDKZHAPOAHSFTSPSKXHOCHWHGDYHEOSCPAKJKSMFMZWUAKKHRYKJGDRZNWDJYTFHVTTOWXMYSBEUYTDSJGRMRMAJZVKFXJTIGPZHXQFISQHGJYQSRZNSKKHHVJHOPIILIUUZDBXKPYZILNQFGWWUIFDUGUQCKRFZNEOXMTZOHWSLKPGXSMRNTZVWRWQAEXTWNAWDJMQOHXZRAOXIDPCLDJETJLJCPPCEBMEIFWYTNKILNOTVVNTQEDPAROFXMUFKKYNHXJYPFTJTVWTILPUHRGXWWCNVMRHKLKGGGRJUKRNNFOFMLDUZVRKVJMVJRMJLPQMOZYCGCUNWAAXSRKLGQXICJOAYKJOWXCOLXTRQNRRQGVOXUWCHYSAQMLPMREIRNOHPTRCXCBEYYGRMLYPRJBLLFFNCDWVKEBBUYHJLGLLKEGGCCLBBPPKGMPMGORKNASRZWQWABXZJIIZVPJUISIANEINBWPTJKPVQNTXSMFLFHRYYUWHYWPTRFWZASYQHTHLMTFVMETHLAFYYMZYAQTWLPYTDAJXOVRQGSPFDXDJWAFPAYNNEESPKWTPWHSVJKINXCCXGLXPJFDZPNDMJZOCFJHEKISNVOJFIPSCHCGAFVVDXCVKZRIFNAGLPBLIBGSBVMUJDWXEZSXOUNFWUFPQZQPYFSPRFRBDQAIIXATTJADDWNHARYVWMBCTIRIGMHZPMQROHWDEOAYTBTWALXPKRPWBSLFROWRMGBWRCCGHMMTMODRBQNXEFBFWHTAWMQTRNFSDIKRKKHOZKFNXPAGFBWUVUTXYMSRHSJLCUUTVXWRVNMXZXOFIRZIMXAXUWTWMURTXVHODPGCVADBXUUCHSGSYSBDSHJUPDGSNPYYDJVMTYCVFNVUBQFBBVQNXTHHAFJJJHAMOSPDOEVACHYBRUIAYKXWRXRPZQCUVOTTUCHJXWVGWQWKVYBWJWWZEZCFMKZAUBFJXACQCMEJOGZWYTPCQKXUQXZMDRVDKBJSMJUCMSWGECVROXIHOAKZUBTEWMTLPOJKITEIILUXIESCHNLDFFLKONYKGJPSCHNYCCMWPWBLMLVEXNKNRSEMYDBXDAYCOFIGCHTUFXTMWJLYYRYYKUYDBGOESBUMBCXVDDRIEYAAAWJDEOXZNHCQSNPANZNBAZUNLLRXJIKBLZKGBVGRZHWQLXFPWLIFCCXOOPBARVBYEJIDSYRKUQXVJIQFGFBVATNIIFTPQAHZPPHCMBAPJGBEVPXEZNOUBIJEKFWAEHEEKTUVHOJNPJVMDWPXXINTLDCDYDNHWIODLQEMPKSFITFUOTWCLOUNJKSCSHZDOABHNPXEQPGDNSAKZMBKVCPSJCEVLUDOMILIYUDRACDBIFKAXEXUQHXZATWOVXTNJNBTFFPAQRPJHIMZWYERERURXTUXWYGQOLJZGIESXJAKXXQXECUYZOWUSVLPGSXHETRPTFVFUERPACNWNESZMPTNHMDXTIVTSUNHEQYYJGPIGJZHNVHWXCPVKZYWKZZVUVKFCUWHVCGDNBUYOWAUPCQOKLRFPJJMFRAIAVZOWBJZNZIWJGPBCTKARNPELTZOQYBPWTOUIFYJXCKVJAPRASCWXLQOHNWGQOXXGSXAITISVAUZPFLVAXRFNRESCKPDIDTQNJGDHQDJMOXBVJELUQIUQVRSUYAZRTFBXNJXADHSMRJVDRJAYMGNRTUTWWZXJEMRBVYMMDVNDXDHHJDQQLDVHAYCAZNFFATVSKDKGMVZXEJZLYHPLYOYYJUTVOMZGXPZTFFUFZIWDPSWNSEEDZGGEDKPUHZORYNGWBZIKXJLZEUMZNKMPJWTZKGQOUXCDMEQFLPINZZMAVRRIIOLDRKEGXJNMVIVIRNILHYFIYOCGFRDDXUGUWIIDYBIVYSHBQOSJMBOUFJFEBMGJJSUWZZPUSRAOWFRGFXKVTYXQOTKAMKPQXUSWOHWDWETBXOZXVWXBBAXQDYVMYUSROHYFTQBJMSUAWXOUXKSEWFMDXQCKGSXEZDSMGZFEHHZJBMJSZPDZKVVCCRXFRVHOLWCSDAFVXRXFAZOJSZXUXLBCZJMVYJEJOSDOBNBUVTWKBEHYNTZTJDBNMJRHVUJJYFRWY"

playera=0
playerb=0
data= []

newdatalist = list(b)

for i in b:
    patt1 = ''
    for j in newdatalist:
        if j.isalpha():
            patt1 = patt1 + j
            print(patt1)
            if patt1[0].lower() not in "aeiou":
                if patt1 not in data:
                    data.append(patt1) 
                    playera = playera + 1
                    print('const ', playera)
                else:
                    playera = playera + 1
                    print('const ', playera)
                    
            
            else:
                if patt1 not in data:
                    data.append(patt1)
                    playerb = playerb + 1
                    print('vowel ',playerb)
                else:
                    playerb = playerb + 1
                    print('vowel ',playerb)

    print(i)
    newdatalist.remove(i) 

    print('\n')
    print(newdatalist)


   
    
    

      
    

print(playera)
print(playerb)



