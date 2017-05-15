# Automatically generated from StableNoise.hip #

import math


def silib_noise_range_lookup(rough, octaves):
    octave_n=10
    roughness_n=20
    
    noise_lookuptable = [ 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543, 0.5401148796081543,
        0.5401148796081543, 0.5401148796081543, 0.540108859539032, 0.5401028394699097, 0.5400968194007874, 0.540090799331665, 0.5435646772384644, 0.5506804585456848, 0.5577962398529053, 0.5649120211601257, 0.5720278024673462, 0.5804221630096436, 0.5909988880157471, 0.6104412078857422, 0.6298835873603821, 0.6493258476257324, 0.6687682271003723, 0.6882106065750122, 0.7076529264450073, 0.7270952463150024,
        0.7465375661849976, 0.7659798860549927, 0.5401148796081543, 0.5401092767715454, 0.5401045680046082, 0.5401006937026978, 0.5400976538658142, 0.5479493141174316, 0.561496913433075, 0.5759261250495911, 0.5912370085716248, 0.6074293851852417, 0.624503493309021, 0.6424592137336731, 0.6763265132904053, 0.712334156036377, 0.7502398490905762, 0.7900435924530029, 0.8317453861236572, 0.8753452301025391,
        0.920843243598938, 0.9682391881942749, 1.018297791481018, 0.5401148796081543, 0.5401092171669006, 0.5401042103767395, 0.5400994420051575, 0.5400946736335754, 0.5469198822975159, 0.5597180724143982, 0.5731014609336853, 0.5870205760002136, 0.6014258861541748, 0.6312664747238159, 0.6705154776573181, 0.7130656838417053, 0.7590447664260864, 0.8086724281311035, 0.8673899173736572, 0.9306504726409912,
        0.9986719489097595, 1.071673035621643, 1.157227635383606, 1.256075382232666, 0.5401148796081543, 0.5401092171669006, 0.5401041507720947, 0.540099024772644, 0.5400933623313904, 0.5470190048217773, 0.5599236488342285, 0.5734823346138, 0.5876703262329102, 0.6024666428565979, 0.6279777884483337, 0.6657004952430725, 0.7062462568283081, 0.7607920169830322, 0.8286351561546326, 0.9065014123916626,
        0.995427668094635, 1.096510648727417, 1.2109079360961914, 1.3398363590240479, 1.4845739603042603, 0.5401148796081543, 0.5401092171669006, 0.5401041507720947, 0.5400989055633545, 0.540092945098877, 0.5469235181808472, 0.5596860647201538, 0.5729689002037048, 0.5866692662239075, 0.6006627082824707, 0.6307594180107117, 0.6701803803443909, 0.7131679058074951, 0.7735976576805115, 0.8471843004226685,
        0.9326916933059692, 1.0315922498703003, 1.1454805135726929, 1.2760777473449707, 1.4252351522445679, 1.5949395895004272, 0.5401148796081543, 0.5401092171669006, 0.5401041507720947, 0.5400989055633545, 0.5400928854942322, 0.5469627976417542, 0.559803307056427, 0.5732645988464355, 0.5873281359672546, 0.6019983887672424, 0.6259918212890625, 0.662275493144989, 0.7081636190414429, 0.7655568718910217,
        0.83464115858078, 0.9137165546417236, 1.0036437511444092, 1.1052707433700562, 1.2194181680679321, 1.3538023233413696, 1.5676944255828857, 0.5401148796081543, 0.5401092171669006, 0.5401041507720947, 0.5400989055633545, 0.5400928258895874, 0.54696124792099, 0.5597977638244629, 0.5732483267784119, 0.587286651134491, 0.6019037365913391, 0.626522958278656, 0.6627692580223083, 0.7096972465515137,
        0.7727267146110535, 0.846686065196991, 0.9332395195960999, 1.034316062927246, 1.1521574258804321, 1.2893725633621216, 1.4490002393722534, 1.6345818042755127, 0.5401148796081543, 0.5401092171669006, 0.5401041507720947, 0.5400989055633545, 0.5400928258895874, 0.5469611287117004, 0.5597972869873047, 0.5732466578483582, 0.5872818827629089, 0.6018914580345154, 0.6246169805526733, 0.6604396104812622,
        0.7124853730201721, 0.778016209602356, 0.8562555909156799, 0.9498581886291504, 1.0621660947799683, 1.1973906755447388, 1.3608298301696777, 1.5591275691986084, 1.8005810976028442, 0.5401148796081543, 0.5401092171669006, 0.5401041507720947, 0.5400989055633545, 0.5400928258895874, 0.5469602942466736, 0.5597928166389465, 0.5732287764549255, 0.5872225165367126, 0.6017200350761414, 0.6248550415039062,
        0.6608074903488159, 0.7103241086006165, 0.7735742926597595, 0.8476012349128723, 0.9337552785873413, 1.0333813428878784, 1.1477173566818237, 1.2922438383102417, 1.5747560262680054, 1.950214147567749 ]
    
    if octaves>octave_n:
        octaves=octave_n
    
    octave_idx = (octaves-1)*(roughness_n+1)
    rough_idx = int(math.floor(rough*roughness_n))
    frac = rough*roughness_n - math.floor(rough*roughness_n)
    
    idx = octave_idx + rough_idx
    rough_idx_next = rough_idx+1
    if rough_idx_next==roughness_n+1:
        rough_idx_next = rough_idx
    idx_next = octave_idx + rough_idx_next
  
    amp_out = (1.0-frac)*noise_lookuptable[idx] + frac*noise_lookuptable[idx_next]
    return amp_out

def silib_xnoise_range_lookup(rough, octaves):
    octave_n=10
    roughness_n=20
    
    xnoise_lookuptable = [ 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813, 0.8057247400283813,
        0.8057247400283813, 0.8057247400283813, 0.8199519515037537, 0.8341792225837708, 0.8484064340591431, 0.8626336455345154, 0.8768608570098877, 0.8910881280899048, 0.9053153395652771, 0.9195425510406494, 0.9337698221206665, 0.9479970335960388, 0.9722009897232056, 1.0019900798797607, 1.0317792892456055, 1.0615684986114502, 1.091357707977295, 1.12114679813385, 1.1509360074996948, 1.1807252168655396,
        1.2105143070220947, 1.2403035163879395, 0.8057247400283813, 0.8198690414428711, 0.83384770154953, 0.847660481929779, 0.8613075613975525, 0.8747888207435608, 0.8881043791770935, 0.9012541174888611, 0.9142380952835083, 0.9282819032669067, 0.9676178693771362, 1.0083866119384766, 1.0505881309509277, 1.0942225456237793, 1.1392897367477417, 1.185789704322815, 1.233722448348999, 1.2830878496170044,
        1.3338862657546997, 1.3943842649459839, 1.4697564840316772, 0.8057247400283813, 0.819802463054657, 0.8333151340484619, 0.8458631634712219, 0.8570472002029419, 0.8664677739143372, 0.8737255930900574, 0.8784211874008179, 0.8820590972900391, 0.9131134748458862, 0.9448337554931641, 0.9773287773132324, 1.0107074975967407, 1.0514461994171143, 1.1006133556365967, 1.1634811162948608, 1.2353992462158203,
        1.3342463970184326, 1.4447002410888672, 1.5630111694335938, 1.68949556350708, 0.8057247400283813, 0.8198038339614868, 0.8333366513252258, 0.8459720611572266, 0.8573912978172302, 0.8673079013824463, 0.8754676580429077, 0.8816485404968262, 0.8949866890907288, 0.9338209629058838, 0.9763951897621155, 1.0235378742218018, 1.07615327835083, 1.1352217197418213, 1.205230474472046, 1.3075714111328125,
        1.4219295978546143, 1.54948890209198, 1.6915016174316406, 1.849287986755371, 2.0242366790771484, 0.8057247400283813, 0.8198038935661316, 0.83333820104599, 0.8459839820861816, 0.8574416637420654, 0.8674615621566772, 0.8758499622344971, 0.8824748992919922, 0.8957920074462891, 0.935272216796875, 0.9788528680801392, 1.0274959802627563, 1.0822688341140747, 1.1443469524383545, 1.2150168418884277,
        1.2956790924072266, 1.387851357460022, 1.4931716918945312, 1.6720247268676758, 1.8937604427337646, 2.1478018760681152, 0.8057247400283813, 0.8198038935661316, 0.83333820104599, 0.8459842205047607, 0.8574428558349609, 0.8674660325050354, 0.8758633732795715, 0.8825086951255798, 0.8971658945083618, 0.9380574226379395, 0.9840937256813049, 1.0367804765701294, 1.097917914390564, 1.169643521308899,
        1.254478096961975, 1.3553757667541504, 1.475778341293335, 1.619673252105713, 1.7916535139083862, 2.081700563430786, 2.4304304122924805, 0.8057247400283813, 0.8198038935661316, 0.83333820104599, 0.8459840416908264, 0.8574416041374207, 0.8674601316452026, 0.875842273235321, 0.8824466466903687, 0.8973511457443237, 0.9384799599647522, 0.984977126121521, 1.0385019779205322, 1.1010832786560059,
        1.1751867532730103, 1.2637903690338135, 1.370469570159912, 1.4994920492172241, 1.655922770500183, 1.8457374572753906, 2.1110942363739014, 2.530076742172241, 0.8057247400283813, 0.8198038935661316, 0.83333820104599, 0.8459840416908264, 0.857441782951355, 0.8674610257148743, 0.8758462071418762, 0.8824601769447327, 0.8975195288658142, 0.938912034034729, 0.9859808683395386, 1.0406535863876343,
        1.1053991317749023, 1.1833745241165161, 1.278603434562683, 1.3961942195892334, 1.542602300643921, 1.7259410619735718, 1.9563490152359009, 2.24642014503479, 2.74474835395813, 0.8057247400283813, 0.8198038935661316, 0.83333820104599, 0.8459840416908264, 0.8574419021606445, 0.8674619793891907, 0.8758512139320374, 0.8824802041053772, 0.8975462317466736, 0.9389890432357788, 0.9861797094345093,
        1.0411224365234375, 1.1064250469207764, 1.1854829788208008, 1.282711386680603, 1.40383780002594, 1.5562655925750732, 1.7495194673538208, 1.9957882165908813, 2.383502244949341, 2.9675064086914062 ]
    
    if octaves>octave_n:
        octaves=octave_n
    
    octave_idx = (octaves-1)*(roughness_n+1)
    rough_idx = int(math.floor(rough*roughness_n))
    frac = rough*roughness_n - math.floor(rough*roughness_n)
    
    idx = octave_idx + rough_idx
    rough_idx_next = rough_idx+1
    if rough_idx_next==roughness_n+1:
        rough_idx_next = rough_idx
    idx_next = octave_idx + rough_idx_next
  
    amp_out = (1.0-frac)*xnoise_lookuptable[idx] + frac*xnoise_lookuptable[idx_next]
    return amp_out

def silib_onoise_range_lookup(rough, octaves):
    octave_n=10
    roughness_n=20
    
    onoise_lookuptable = [ 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645, 0.7050517201423645,
        0.7050517201423645, 0.7050517201423645, 0.7050550580024719, 0.7050598859786987, 0.7050647139549255, 0.7050694823265076, 0.711104691028595, 0.7279191017150879, 0.7447335720062256, 0.7615479826927185, 0.7810841202735901, 0.809825599193573, 0.8385671377182007, 0.8673086166381836, 0.8960500955581665, 0.9247915744781494, 0.9535330533981323, 0.98227459192276, 1.0110161304473877, 1.0397576093673706,
        1.0684990882873535, 1.0972405672073364, 0.7050517201423645, 0.7050546407699585, 0.7050582766532898, 0.7050610780715942, 0.705062985420227, 0.7214816808700562, 0.7428619265556335, 0.7650724649429321, 0.7881130576133728, 0.8119837641716003, 0.8385336399078369, 0.8729361891746521, 0.9101256728172302, 0.9501023888587952, 0.992866039276123, 1.038416862487793, 1.0867547988891602, 1.137879729270935,
        1.1928493976593018, 1.253704309463501, 1.3174848556518555, 0.7050517201423645, 0.7050546407699585, 0.7050581574440002, 0.7050607204437256, 0.705062210559845, 0.7202019691467285, 0.7406505942344666, 0.7615609765052795, 0.782871425151825, 0.8134657144546509, 0.8517236709594727, 0.8915880918502808, 0.9331739544868469, 0.9765965938568115, 1.0219712257385254, 1.0694133043289185, 1.1190379858016968,
        1.1709603071212769, 1.2684884071350098, 1.3819701671600342, 1.5039117336273193, 0.7050517201423645, 0.7050546407699585, 0.7050580382347107, 0.7050600051879883, 0.7050598859786987, 0.7193693518638611, 0.7389240264892578, 0.758362352848053, 0.7774146795272827, 0.8133476376533508, 0.851543664932251, 0.8913245797157288, 0.9328007102012634, 0.9773827791213989, 1.043116569519043, 1.1173207759857178,
        1.200960397720337, 1.2950422763824463, 1.4020168781280518, 1.5601592063903809, 1.739272117614746, 0.7050517201423645, 0.7050546407699585, 0.7050580382347107, 0.705059826374054, 0.7050592303276062, 0.7195653915405273, 0.7394118309020996, 0.7594166994094849, 0.7819861173629761, 0.8230085968971252, 0.867904543876648, 0.9176740050315857, 0.9735118746757507, 1.0368293523788452, 1.1093028783798218,
        1.192845344543457, 1.2896183729171753, 1.402098536491394, 1.533077359199524, 1.6856800317764282, 1.863387107849121, 0.7050517201423645, 0.7050546407699585, 0.7050580382347107, 0.705059826374054, 0.7050593495368958, 0.7194708585739136, 0.7391294836997986, 0.7587047219276428, 0.7823363542556763, 0.8237185478210449, 0.8692404627799988, 0.9200407266616821, 0.9775009751319885, 1.0432777404785156,
        1.1193314790725708, 1.2079600095748901, 1.311828374862671, 1.4340049028396606, 1.5779950618743896, 1.7518314123153687, 2.0304033756256104, 0.7050517201423645, 0.7050546407699585, 0.7050580382347107, 0.705059826374054, 0.705059289932251, 0.7194696068763733, 0.7391250133514404, 0.7586915493011475, 0.7828421592712402, 0.8248721361160278, 0.8716523051261902, 0.924740731716156, 0.9861431121826172,
        1.0584118366241455, 1.1447557210922241, 1.249168872833252, 1.3765711784362793, 1.5329726934432983, 1.7256537675857544, 1.9633655548095703, 2.2565536499023438, 0.7050517201423645, 0.7050546407699585, 0.7050580382347107, 0.705059826374054, 0.7050593495368958, 0.7194632887840271, 0.7390978336334229, 0.758598268032074, 0.7828482985496521, 0.8248879313468933, 0.8716890215873718, 0.9248194098472595,
        0.9863008856773376, 1.0587111711502075, 1.1452972888946533, 1.250109314918518, 1.3781472444534302, 1.5355324745178223, 1.7296974658966064, 1.969597578048706, 2.317314624786377, 0.7050517201423645, 0.7050546407699585, 0.7050580382347107, 0.705059826374054, 0.7050593495368958, 0.719461977481842, 0.7390910387039185, 0.7585710883140564, 0.7828519940376282, 0.8248986601829529, 0.8717166781425476,
        0.924884557723999, 0.9864434599876404, 1.0590041875839233, 1.145868182182312, 1.251171588897705, 1.380046010017395, 1.5388091802597046, 1.7351783514022827, 2.1019604206085205, 2.6051104068756104 ]
    
    if octaves>octave_n:
        octaves=octave_n
    
    octave_idx = (octaves-1)*(roughness_n+1)
    rough_idx = int(math.floor(rough*roughness_n))
    frac = rough*roughness_n - math.floor(rough*roughness_n)
    
    idx = octave_idx + rough_idx
    rough_idx_next = rough_idx+1
    if rough_idx_next==roughness_n+1:
        rough_idx_next = rough_idx
    idx_next = octave_idx + rough_idx_next
  
    amp_out = (1.0-frac)*onoise_lookuptable[idx] + frac*onoise_lookuptable[idx_next]
    return amp_out

def silib_snoise_range_lookup(rough, octaves):
    octave_n=10
    roughness_n=20
    
    snoise_lookuptable = [ 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664, 1.409799575805664,
        1.409799575805664, 1.393721342086792, 1.377644419670105, 1.3638134002685547, 1.354697823524475, 1.3455822467803955, 1.3364665508270264, 1.3273509740829468, 1.3182353973388672, 1.3091198205947876, 1.3139681816101074, 1.3382666110992432, 1.3802249431610107, 1.4482303857803345, 1.5170440673828125, 1.587533950805664, 1.6580238342285156, 1.7285138368606567, 1.7990037202835083, 1.8694936037063599,
        1.9399834871292114, 1.409799575805664, 1.3939805030822754, 1.3786811828613281, 1.3647311925888062, 1.3563294410705566, 1.3481316566467285, 1.3401377201080322, 1.3323478698730469, 1.3323720693588257, 1.375686764717102, 1.422103762626648, 1.471623420715332, 1.5242455005645752, 1.579970121383667, 1.6387970447540283, 1.7007266283035278, 1.7657588720321655, 1.8338934183120728, 1.9222290515899658,
        2.0660128593444824, 2.2164628505706787, 1.409799575805664, 1.3939827680587769, 1.3786988258361816, 1.3650493621826172, 1.3570835590362549, 1.3496044874191284, 1.3426828384399414, 1.3363893032073975, 1.3307945728302002, 1.359528660774231, 1.399938941001892, 1.4421221017837524, 1.4859447479248047, 1.5312740802764893, 1.5779768228530884, 1.6453053951263428, 1.796660304069519, 1.9598710536956787,
        2.135444402694702, 2.3238863945007324, 2.5257039070129395, 1.409799575805664, 1.3939813375473022, 1.3786768913269043, 1.3650879859924316, 1.3572055101394653, 1.3499022722244263, 1.3433003425598145, 1.3375332355499268, 1.3327460289001465, 1.3490220308303833, 1.383925199508667, 1.4186762571334839, 1.4527385234832764, 1.485537052154541, 1.5864421129226685, 1.7038003206253052, 1.8341072797775269,
        1.9921271800994873, 2.1759865283966064, 2.3810336589813232, 2.6313412189483643, 1.409799575805664, 1.3939813375473022, 1.3786773681640625, 1.3650755882263184, 1.357153296470642, 1.349743127822876, 1.3429042100906372, 1.336677074432373, 1.3310768604278564, 1.3554165363311768, 1.394754409790039, 1.4361168146133423, 1.4796850681304932, 1.525745153427124, 1.5858176946640015, 1.7546826601028442,
        1.9515185356140137, 2.180135726928711, 2.4447343349456787, 2.7499215602874756, 3.1007349491119385, 1.409799575805664, 1.3939813375473022, 1.3786773681640625, 1.3650743961334229, 1.3571466207504272, 1.3497177362442017, 1.3428282737731934, 1.3364856243133545, 1.3306503295898438, 1.3586370944976807, 1.400814414024353, 1.446852445602417, 1.4977799654006958, 1.5549954175949097, 1.6203289031982422,
        1.8027613162994385, 2.0223333835601807, 2.282017946243286, 2.588296413421631, 2.9484972953796387, 3.3708722591400146, 1.409799575805664, 1.3939813375473022, 1.3786773681640625, 1.3650752305984497, 1.3571524620056152, 1.3497456312179565, 1.342928171157837, 1.3367795944213867, 1.3313990831375122, 1.3605440855026245, 1.404801368713379, 1.4546220302581787, 1.512066125869751, 1.5800132751464844,
        1.662357211112976, 1.7991583347320557, 2.0166726112365723, 2.273364782333374, 2.5753860473632812, 2.9780235290527344, 3.5632412433624268, 1.409799575805664, 1.3939813375473022, 1.3786773681640625, 1.3650753498077393, 1.3571537733078003, 1.349753499031067, 1.3429620265960693, 1.3368957042694092, 1.3317371606826782, 1.3605024814605713, 1.4047048091888428, 1.4544150829315186, 1.5116509199142456,
        1.5792256593704224, 1.6609323024749756, 1.82071053981781, 2.052790641784668, 2.332026481628418, 2.6680569648742676, 3.164053440093994, 3.8439598083496094, 1.409799575805664, 1.3939813375473022, 1.3786773681640625, 1.3650753498077393, 1.3571537733078003, 1.3497533798217773, 1.3429615497589111, 1.3368936777114868, 1.3317304849624634, 1.3605225086212158, 1.4047565460205078, 1.4545371532440186,
        1.511918067932129, 1.5797747373580933, 1.6620020866394043, 1.8368747234344482, 2.0816850662231445, 2.3818888664245605, 2.7514607906341553, 3.2385082244873047, 3.9847605228424072 ]
    
    if octaves>octave_n:
        octaves=octave_n
    
    octave_idx = (octaves-1)*(roughness_n+1)
    rough_idx = int(math.floor(rough*roughness_n))
    frac = rough*roughness_n - math.floor(rough*roughness_n)
    
    idx = octave_idx + rough_idx
    rough_idx_next = rough_idx+1
    if rough_idx_next==roughness_n+1:
        rough_idx_next = rough_idx
    idx_next = octave_idx + rough_idx_next
  
    amp_out = (1.0-frac)*snoise_lookuptable[idx] + frac*snoise_lookuptable[idx_next]
    return amp_out

def silib_anoise_range_lookup(rough, octaves):
    octave_n=10
    roughness_n=20
    
    anoise_lookuptable = [ 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865, 0.8927037715911865,
        0.8927037715911865, 0.8927037715911865, 0.8992387056350708, 0.9057736396789551, 0.9123085737228394, 0.9244965314865112, 0.940380871295929, 0.9618507623672485, 0.9833205938339233, 1.0047905445098877, 1.0262603759765625, 1.0477302074432373, 1.069200038909912, 1.0906699895858765, 1.1121398210525513, 1.133609652519226, 1.1550796031951904, 1.1765494346618652, 1.19801926612854, 1.2194892168045044,
        1.2409590482711792, 1.262428879737854, 0.8927037715911865, 0.8992570638656616, 0.9058471918106079, 0.91692054271698, 0.9354193210601807, 0.9552834033966064, 0.9804249405860901, 1.0090186595916748, 1.0396924018859863, 1.0724480152130127, 1.1072851419448853, 1.1442022323608398, 1.1831995248794556, 1.2242770195007324, 1.2674344778060913, 1.3126720190048218, 1.3599897623062134, 1.409387469291687,
        1.4608656167984009, 1.5144234895706177, 1.5700616836547852, 0.8927037715911865, 0.8992680907249451, 0.9059351682662964, 0.9171291589736938, 0.9359138011932373, 0.9562491178512573, 0.9809370636940002, 1.0098319053649902, 1.040906310081482, 1.0741758346557617, 1.1096552610397339, 1.1473569869995117, 1.1872951984405518, 1.2294843196868896, 1.2739382982254028, 1.3206713199615479, 1.3696980476379395,
        1.458282232284546, 1.5758477449417114, 1.7043685913085938, 1.8443068265914917, 0.8927037715911865, 0.8992680907249451, 0.9059351682662964, 0.9171459078788757, 0.9359667301177979, 0.9563783407211304, 0.9825389385223389, 1.012799620628357, 1.0459731817245483, 1.0822947025299072, 1.1220297813415527, 1.1654744148254395, 1.2129548788070679, 1.2648271322250366, 1.3214761018753052, 1.3833171129226685,
        1.4507954120635986, 1.5243850946426392, 1.637873649597168, 1.7830250263214111, 1.9474235773086548, 0.8927037715911865, 0.8992680907249451, 0.9059356451034546, 0.9171468019485474, 0.9359704256057739, 0.9563896059989929, 0.9825419783592224, 1.0128061771392822, 1.0459866523742676, 1.0823190212249756, 1.1220710277557373, 1.1655409336090088, 1.213057518005371, 1.2649803161621094, 1.3216980695724487,
        1.3836305141448975, 1.451228141784668, 1.5454609394073486, 1.6591730117797852, 1.7890359163284302, 2.0842041969299316, 0.8927037715911865, 0.8992680907249451, 0.9059357047080994, 0.9171468019485474, 0.9359706044197083, 0.9563902020454407, 0.9825782179832458, 1.0128976106643677, 1.0461903810501099, 1.0827322006225586, 1.122848391532898, 1.166918158531189, 1.215378761291504, 1.2687326669692993,
        1.3458826541900635, 1.460679054260254, 1.5997226238250732, 1.768487811088562, 1.9734472036361694, 2.2221884727478027, 2.5235424041748047, 0.8927037715911865, 0.8992680907249451, 0.9059357047080994, 0.9171468019485474, 0.9359706044197083, 0.9563902020454407, 0.9825783967971802, 1.0128980875015259, 1.0461921691894531, 1.0827363729476929, 1.1228572130203247, 1.1669352054595947, 1.2154101133346558,
        1.2687876224517822, 1.345930576324463, 1.4607566595077515, 1.5998445749282837, 1.7686742544174194, 1.973725438117981, 2.222594738006592, 2.5241241455078125, 0.8927037715911865, 0.8992680907249451, 0.9059357047080994, 0.9171468019485474, 0.9359706044197083, 0.9563902020454407, 0.9825859069824219, 1.0129239559173584, 1.046265721321106, 1.0829249620437622, 1.1232954263687134, 1.1678745746612549,
        1.217294454574585, 1.272363543510437, 1.352622151374817, 1.4723774194717407, 1.619318962097168, 1.8003040552139282, 2.0236926078796387, 2.2996022701263428, 2.640200614929199, 0.8927037715911865, 0.8992680907249451, 0.9059357047080994, 0.9171468019485474, 0.9359706044197083, 0.9563902616500854, 0.9825860261917114, 1.0129244327545166, 1.0462661981582642, 1.0829261541366577, 1.1232985258102417,
        1.1678858995437622, 1.217341661453247, 1.2724870443344116, 1.3529754877090454, 1.4730602502822876, 1.6205812692642212, 1.802542805671692, 2.0275192260742188, 2.3059349060058594, 2.6503849029541016 ]
    
    if octaves>octave_n:
        octaves=octave_n
    
    octave_idx = (octaves-1)*(roughness_n+1)
    rough_idx = int(math.floor(rough*roughness_n))
    frac = rough*roughness_n - math.floor(rough*roughness_n)
    
    idx = octave_idx + rough_idx
    rough_idx_next = rough_idx+1
    if rough_idx_next==roughness_n+1:
        rough_idx_next = rough_idx
    idx_next = octave_idx + rough_idx_next
  
    amp_out = (1.0-frac)*anoise_lookuptable[idx] + frac*anoise_lookuptable[idx_next]
    return amp_out
