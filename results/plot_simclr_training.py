from matplotlib import pyplot as plt

# without projection head
eight_loss = [9.126749992370605, 8.062483787536621, 6.69362735748291, 6.223260879516602, 6.162203788757324,
              6.118102073669434, 6.077719688415527, 5.99798583984375, 6.134178638458252, 6.09935998916626,
              6.078614234924316, 6.068822860717773, 6.0441389083862305, 6.0790228843688965, 6.004064559936523,
              5.99912166595459, 6.140353679656982, 6.017667770385742, 5.966787338256836, 6.022122859954834,
              5.957648277282715, 5.864597320556641, 5.935187339782715, 5.911531448364258, 5.8170247077941895,
              5.914128303527832, 5.891658306121826, 5.824912071228027, 5.843649387359619, 5.845293998718262,
              5.897711277008057, 5.842360019683838, 5.835693359375, 5.802269458770752, 5.823354721069336,
              5.839217185974121, 5.793741703033447, 5.8206562995910645, 5.826458930969238, 5.810474395751953,
              5.720738410949707, 5.850881576538086, 5.831172943115234, 5.709168910980225, 5.7785468101501465,
              5.768893718719482, 5.740474700927734, 5.674448490142822, 5.770069122314453, 5.682681083679199,
              5.726676940917969, 5.7638020515441895, 5.702191352844238, 5.745002269744873, 5.622068881988525,
              5.658740997314453, 5.623608589172363, 5.609984397888184, 5.6871185302734375, 5.605518817901611,
              5.662929534912109, 5.607845306396484, 5.669044494628906, 5.6702375411987305, 5.617611885070801,
              5.545267105102539, 5.5425262451171875, 5.591949939727783, 5.574445724487305, 5.519317150115967,
              5.557380199432373, 5.6533403396606445, 5.547530651092529, 5.552243232727051, 5.600050926208496,
              5.534585952758789, 5.450079917907715, 5.631026268005371, 5.556378364562988, 5.389601230621338,
              5.555598735809326, 5.471927642822266, 5.488224983215332, 5.399659156799316, 5.3745436668396,
              5.356141567230225, 5.289960861206055, 5.430759906768799, 5.333007335662842, 5.257528305053711,
              5.4284987449646, 5.294611930847168, 5.348533630371094, 5.323570251464844, 5.377156734466553,
              5.248130798339844, 5.320923805236816, 5.261929035186768, 5.406234264373779, 5.163905620574951,
              5.3133673667907715, 5.201998233795166, 5.2413330078125, 5.257350921630859, 5.16849422454834,
              5.164427757263184, 5.108191013336182, 5.1922502517700195, 5.01925802230835, 5.13064432144165,
              5.110198974609375, 5.097215175628662, 5.254144668579102, 5.397352695465088, 5.243433475494385,
              5.041720390319824, 5.301784038543701, 5.2263031005859375, 5.292895793914795, 5.283433437347412,
              5.102992057800293, 5.130510330200195, 5.036375999450684, 5.119968414306641, 5.053353786468506,
              5.130442142486572, 5.191246509552002, 5.0351243019104, 5.056406021118164, 5.131664276123047,
              5.0382843017578125, 5.083472728729248, 5.007424831390381, 5.092374324798584, 5.030495643615723,
              5.119495868682861, 4.9984660148620605, 5.176274299621582, 5.080964088439941, 5.165682792663574,
              5.086502552032471, 4.96432638168335, 4.92338228225708, 5.094870090484619, 4.90027379989624,
              5.058619499206543, 4.899738311767578, 5.042501926422119, 4.946451663970947, 4.9458441734313965,
              5.067413806915283, 4.893964767456055, 4.803816795349121, 4.9736409187316895, 4.951994895935059,
              4.894350051879883, 4.826421737670898, 5.061811447143555, 5.087394714355469, 4.836055278778076,
              5.048745632171631, 4.8811211585998535, 4.795921325683594, 5.091859340667725, 5.050535202026367,
              4.860109329223633, 4.767704486846924, 4.846862316131592, 4.980952262878418]
eight_overlap = [0.5487405986429842, 0.522795335122467, 0.569568961054216, 0.6734876578365869, 0.7236254137066491,
                 0.7607720877868218, 0.7703048377528898, 0.7791615939188399, 0.7237570269489035, 0.7552517231602871,
                 0.7677530146239564, 0.7936376833683585, 0.7864313256087335, 0.7562343061498232, 0.7423484161858976,
                 0.7278901715347719, 0.6664381263861769, 0.6863089272547104, 0.7240888942902204, 0.7028363825012537,
                 0.7145952991641927, 0.721607814900283, 0.7052301483265779, 0.6638659931295032, 0.711629820974883,
                 0.6699100974346532, 0.6737509185927081, 0.6847815022434117, 0.6940883413400397, 0.6909725367430606,
                 0.6599608759325801, 0.7025390670740058, 0.7014321293973558, 0.7081549285989333, 0.6868191943655466,
                 0.6728376229874505, 0.6797341653273017, 0.6599907938436056, 0.6491180905642764, 0.6669591200136544,
                 0.6957044962259415, 0.6662209130736516, 0.6652854277077782, 0.7164115095428152, 0.6845236068109992,
                 0.6888380944719934, 0.6994927389830093, 0.7098376440639333, 0.6394471213604703, 0.6690716047867358,
                 0.6585842234169119, 0.638300963516865, 0.6569438465624029, 0.6464742205851606, 0.6842923850766087,
                 0.6474804826929781, 0.6673883334284748, 0.6866505899598989, 0.6753873072029171, 0.6851005618465467,
                 0.6775669673783365, 0.684836696425361, 0.6469292609084305, 0.6757506429708173, 0.667735257928523,
                 0.6804099455492717, 0.6770080069514566, 0.6673250782685602, 0.6663333760411199, 0.6768358911595607,
                 0.6727867109416481, 0.6634177592337696, 0.676118308994865, 0.6699224978683759, 0.6702885870007675,
                 0.6969532467906936, 0.7062650172650202, 0.6800462091955017, 0.7149020199751219, 0.7234104135754171,
                 0.7113092934262812, 0.6938342389400896, 0.6878923001216277, 0.7180562037852147, 0.7216827699957171,
                 0.7237570565055521, 0.7113871096714595, 0.6927185304117929, 0.6962892749103181, 0.718352182032586,
                 0.6969611882125505, 0.6881637664671616, 0.6825212184158163, 0.6930233009065132, 0.6852872736256641,
                 0.696352668529062, 0.6844643544998223, 0.6704700317765252, 0.6638357422092571, 0.7019480974607988,
                 0.6956968923242196, 0.7112738172397896, 0.7033374046696246, 0.6988895543048682, 0.7275533035315092,
                 0.6977873244120697, 0.7106004352315096, 0.6683968658146735, 0.6849157051722053, 0.6656334483624701,
                 0.660056052241872, 0.6529710072472946, 0.6534262216946299, 0.6132480844250033, 0.6209970278499695,
                 0.704979066872652, 0.6791707395222057, 0.6783433076355293, 0.6670586408280897, 0.6924033182702571,
                 0.7220487516192136, 0.7094570572016765, 0.7400441040566468, 0.6894110051261738, 0.7144397817979009,
                 0.6798197555272109, 0.6659218132197959, 0.6600348915263221, 0.6911281611361577, 0.6995712846002899,
                 0.6999199380456174, 0.7229705932027615, 0.7355640590059878, 0.696759509816417, 0.7157561609813209,
                 0.695387776244458, 0.6943882179989942, 0.6569504615968966, 0.6988838657224727, 0.6870375010282918,
                 0.7042762773996245, 0.7102925608327899, 0.7298778964881574, 0.704999916054722, 0.7388217857009927,
                 0.680924964347801, 0.7083632783379559, 0.6675600971841239, 0.6830157392410031, 0.6858558126802561,
                 0.6731370758336551, 0.7050656518423237, 0.7009914898137994, 0.6957297894989873, 0.6929771312991082,
                 0.7195482354315332, 0.7267687765445126, 0.7132930731993452, 0.6942603979639823, 0.7314358086766811,
                 0.7148945576968884, 0.7299573020588404, 0.7417631321191119, 0.7016242400100905, 0.7002650371968997,
                 0.7002586592557397, 0.744603340329114, 0.7127899507742754, 0.720520801205045]
eight_dhs_pos = [[0.7743702993214915, 0.5402235718481211, 0.5393017343383835, 0.2359904024928457],
                 [0.7613976675612332, 0.4906728968662236, 0.48960705131230636, 0.2728564618028442],
                 [0.7847844805271088, 0.5070268487934462, 0.505933314810243, 0.2799446997000693],
                 [0.8367438289182932, 0.617301212602275, 0.6164372652939443, 0.2211705109326797],
                 [0.8618127068533241, 0.6559669098311833, 0.655156493307474, 0.20746663006955945],
                 [0.8803860438934118, 0.6717281282605252, 0.6709066404037028, 0.21030089134653135],
                 [0.8851524188764446, 0.6446270962553708, 0.6436801461663115, 0.24241922279919242],
                 [0.8895807969594198, 0.6189567261986689, 0.6178912771011857, 0.2727549689557174],
                 [0.861878513474452, 0.5897517724461838, 0.5886804073240253, 0.2742694712725853],
                 [0.8776258615801434, 0.6249116238899167, 0.6239166859462544, 0.2547041135775513],
                 [0.8838765073119779, 0.6554981589144075, 0.6545990315585115, 0.23017660310936228],
                 [0.89681884168418, 0.6634206886657862, 0.6625017982995721, 0.23523593375082208],
                 [0.893215662804367, 0.6401835087264108, 0.6391873191434267, 0.2550245332439245],
                 [0.8781171530749113, 0.5936849834008868, 0.5925651717092568, 0.2866717930572845],
                 [0.871174208092948, 0.5519425568692884, 0.5506857393447857, 0.32174528627266485],
                 [0.8639450857673859, 0.5352174025086245, 0.5339231990312278, 0.331316090213555],
                 [0.8332190631930882, 0.5063738391579766, 0.5050870469373661, 0.32941880847633287],
                 [0.8431544636273549, 0.5180510007005577, 0.5167710658071452, 0.3276633327136224],
                 [0.8620444471451094, 0.5191273442229305, 0.5177772768885912, 0.3456172375908575],
                 [0.8514181912506269, 0.5201197836883396, 0.5188154592491179, 0.3339070564407306],
                 [0.8572976495820968, 0.5062613631089109, 0.5048793304850006, 0.3538003517210064],
                 [0.8608039074501417, 0.48307445202002497, 0.4815873281797489, 0.3807037031106688],
                 [0.8526150741632896, 0.4575551711610161, 0.4559998172121883, 0.3981706108999292],
                 [0.8319329965647521, 0.4207765343988845, 0.4191578081698851, 0.41439391462386643],
                 [0.8558149104874411, 0.4191887425124622, 0.4174697418511434, 0.4400641692976165],
                 [0.8349550487173266, 0.4165267398449657, 0.41487938429822413, 0.42172301996584405],
                 [0.8368754592963542, 0.40929660370562865, 0.4076132223844052, 0.43094561823317235],
                 [0.8423907511217053, 0.41685523460419227, 0.4151798979249895, 0.4288861898759186],
                 [0.8470441706700205, 0.4152932919914113, 0.41359348538244034, 0.435150491896551],
                 [0.84548626837153, 0.42353607955799943, 0.4218748583421982, 0.4252726312451331],
                 [0.8299804379662894, 0.41656767027259206, 0.4149400609509633, 0.4166679863369549],
                 [0.8512695335370033, 0.42437845658964024, 0.42269778305835143, 0.43025242400994057],
                 [0.8507160646986774, 0.4269381916689057, 0.42526977484595385, 0.4271147066756755],
                 [0.8540774642994662, 0.4192795764012184, 0.41756777369295756, 0.43822149331476934],
                 [0.8434095971827729, 0.41684484603887045, 0.41516545725483933, 0.4299235287119647],
                 [0.836418811493725, 0.3971829403673871, 0.39545366528421255, 0.44269442129268705],
                 [0.8398670826636503, 0.38194100341441783, 0.3801381448346965, 0.46153179640867525],
                 [0.8299953969218025, 0.3809960634019103, 0.3792283494904146, 0.4525347613428835],
                 [0.8245590452821385, 0.38107644624536097, 0.37933045176096425, 0.44697458800557105],
                 [0.8334795600068275, 0.3769730118416997, 0.37517574196703385, 0.46010108791445953],
                 [0.8478522481129709, 0.37594939965738844, 0.3740915144272483, 0.47561861891586266],
                 [0.8331104565368257, 0.38719636016841125, 0.3854407928598742, 0.4494252309854887],
                 [0.832642713853889, 0.383817229517136, 0.38205020005124324, 0.45235954326853844],
                 [0.8582057547714077, 0.3954147724433422, 0.3935927607018931, 0.46643500581096364],
                 [0.8422618034054992, 0.3977641619574471, 0.3960141712430847, 0.4479976228767768],
                 [0.8444190472359963, 0.4031022939271979, 0.401364826394486, 0.44479168837422217],
                 [0.8497463694915051, 0.39195151710255877, 0.3901491751640196, 0.4613995362660246],
                 [0.8549188220319671, 0.38686929347244614, 0.3850265787930779, 0.47173495791825737],
                 [0.8197235606802357, 0.3566965268976666, 0.35487358581978246, 0.4666729159383375],
                 [0.8345358023933681, 0.3613851388167374, 0.3595223409286404, 0.4768762593528246],
                 [0.8292921117084564, 0.349495441847071, 0.34760647857990024, 0.4835745963957269],
                 [0.8191504817584323, 0.34235841186049376, 0.3404812777270373, 0.4805463381648515],
                 [0.8284719232812017, 0.33752317938696397, 0.3355903103165142, 0.4948144820351373],
                 [0.8232371102925805, 0.3368442331479845, 0.3349293005608011, 0.49022274231896285],
                 [0.842146192538304, 0.33261327172469024, 0.33060723660337676, 0.5135449910562409],
                 [0.8237402413464887, 0.31663261829741635, 0.3146361315924987, 0.5111005964589077],
                 [0.8336941667142379, 0.32718579679127546, 0.32519166935063387, 0.5104966248042455],
                 [0.8433252949799489, 0.33089737779269346, 0.32887994504786167, 0.516462782676919],
                 [0.8376936536014589, 0.3445864564940564, 0.3426450895763107, 0.49698993094289395],
                 [0.8425502809232738, 0.3273478176773263, 0.3253194615228147, 0.5192591755549707],
                 [0.8387834836891683, 0.32413033743735764, 0.3221041439481772, 0.5187055332301713],
                 [0.8424183482126805, 0.32861276948023477, 0.3265899128710519, 0.5178512919508114],
                 [0.8234646304542151, 0.3296716443179719, 0.32772757744341985, 0.4976811198853474],
                 [0.8378753214854084, 0.35361980975201934, 0.35171329198928947, 0.48806854725884885],
                 [0.833867628964261, 0.33144842165551935, 0.3294703932802881, 0.5063752640592042],
                 [0.8402049727746361, 0.3354825730040355, 0.3334954769419465, 0.5086965918947787],
                 [0.8385040034757276, 0.3183634002434539, 0.3163156025929331, 0.5242361985333153],
                 [0.8336625391342805, 0.3272187020163393, 0.3252248286418592, 0.5104315838669012],
                 [0.8331666880205595, 0.3144769759565905, 0.3124348904760237, 0.5227738830251026],
                 [0.8384179455797808, 0.3223708117189399, 0.3203391300895665, 0.5201104971195876],
                 [0.836393355470824, 0.33261993002216805, 0.3306365700794568, 0.5077401453340786],
                 [0.8317088796168841, 0.32772124387454604, 0.3257370405842219, 0.5079560423229865],
                 [0.8380591544974325, 0.3312933886620613, 0.3292982478516858, 0.510756047456122],
                 [0.834961248934188, 0.33678349551229914, 0.3348221657744177, 0.5021004128976516],
                 [0.8351442935003844, 0.33758691378983674, 0.3356280264681417, 0.5014751543539377],
                 [0.8484766233953465, 0.3379043357606031, 0.3358942086439308, 0.5145925418680879],
                 [0.8531325086325104, 0.3371617243088795, 0.33513034326823526, 0.5200335464049193],
                 [0.840023104597751, 0.3581917747572132, 0.3562948010176835, 0.48562527731959726],
                 [0.8574510099875607, 0.38817133048470054, 0.3863237726913822, 0.4729747950894969],
                 [0.8617052067877085, 0.36333027174513405, 0.36136816570165936, 0.5022991471295238],
                 [0.8556546467131408, 0.4036528618071723, 0.4018733272209284, 0.45556085407845653],
                 [0.8469171194700448, 0.36274756283348486, 0.36084138347664807, 0.48798191535023355],
                 [0.8439461500608136, 0.3433707724217637, 0.3414000032184604, 0.5045169160456567],
                 [0.8590281018926078, 0.3562491553835542, 0.35426971071225866, 0.5067378358516446],
                 [0.8608413849978579, 0.354707005727615, 0.35271435069111795, 0.5101196893432371],
                 [0.8618785282527761, 0.35173479784479494, 0.349726357961299, 0.5141606101749732],
                 [0.8556935548357298, 0.3428183512432731, 0.34079915752834217, 0.5169135910223186],
                 [0.846359265205896, 0.3396612936517327, 0.3376664197479762, 0.5106877193616763],
                 [0.848144637455159, 0.3158860362928849, 0.3137905299890965, 0.5364496137698511],
                 [0.8591760910162927, 0.3289634395334775, 0.3268759881496869, 0.5343875542503964],
                 [0.8484805941062754, 0.3414991923989059, 0.33950320262840444, 0.5109733812483725],
                 [0.8440818832335802, 0.31583531224721656, 0.31375560133782143, 0.5324059928051539],
                 [0.841260609207908, 0.3256597074404326, 0.3236297826303245, 0.5196607513876916],
                 [0.846511650453256, 0.32355179367579867, 0.32149289660187164, 0.5270776509253114],
                 [0.8426436368128329, 0.3444173449048142, 0.34245582407053066, 0.5021493335765859],
                 [0.8481763342645308, 0.3218191062867573, 0.31974683373566376, 0.5305017730799606],
                 [0.8422321772499108, 0.3255275884389904, 0.3234933184043017, 0.5207731288802977],
                 [0.8352350158882629, 0.29156341464196844, 0.289422975266983, 0.5479524799962652],
                 [0.8319178711046292, 0.31742020490207323, 0.315394623539071, 0.5185488289285602],
                 [0.8509740487303992, 0.31639367341304575, 0.31428902626612704, 0.5387896696111908],
                 [0.8478484461621103, 0.3425959421492444, 0.34060675906257953, 0.5092308701861956],
                 [0.8556369086198943, 0.3600049718390856, 0.3580536650013658, 0.49953455045624817],
                 [0.8516687023348114, 0.34359658072039423, 0.3415962967770303, 0.5120726895011449],
                 [0.8494447771524343, 0.36632151218299025, 0.36441945208468535, 0.48692738516605377],
                 [0.8637766517657549, 0.3651826683770538, 0.3632196999385156, 0.5025199202657775],
                 [0.8488936622060357, 0.32190696207256125, 0.31983221128463424, 0.5311362017093286],
                 [0.8553002176157549, 0.3174905789276377, 0.3153732181454011, 0.5420443602525904],
                 [0.834198432907337, 0.31114627131292055, 0.3090870108342024, 0.5271706825518527],
                 [0.8424578525861022, 0.29164847550438705, 0.28947993464973465, 0.55514645879102],
                 [0.8328167241812345, 0.27834631032316404, 0.27616335593789604, 0.5588363226286066],
                 [0.8300280261209364, 0.28239811998687897, 0.2802420967343827, 0.55194195263905],
                 [0.8264855036236467, 0.2841312920316701, 0.28199603923012684, 0.546624717195063],
                 [0.8267131108473154, 0.2947341388350223, 0.2926397334333991, 0.5361677828155393],
                 [0.806624042212502, 0.2956054300502158, 0.2935935457503642, 0.5150423807619893],
                 [0.8104985139249843, 0.28760702774064156, 0.28554839984227803, 0.5270087419810698],
                 [0.8524895334363257, 0.34451543677936547, 0.34251553876103097, 0.5119738926936293],
                 [0.8395853697611035, 0.3390125453910936, 0.3370417862400306, 0.504514342672136],
                 [0.8391716538177638, 0.34173608403163414, 0.3397776762765707, 0.5013523852962567],
                 [0.8335293204140457, 0.3428204705688056, 0.3408885459631157, 0.4945726990566199],
                 [0.8462016591351289, 0.37883111797914304, 0.37699107647852903, 0.4710506241572141],
                 [0.8610243758096066, 0.38660715892913144, 0.3847393746107044, 0.4781527855173292],
                 [0.8547285286008377, 0.37001931771382485, 0.3681110137339547, 0.48852581884675317],
                 [0.8700220520283236, 0.38837910038331225, 0.3864828682902217, 0.4854354158311925],
                 [0.8447055025630876, 0.33355698369927184, 0.3315445879557135, 0.5151733103509324],
                 [0.8572198908989508, 0.3433933892709865, 0.3413704502881993, 0.5178723795935388],
                 [0.8399098777636058, 0.3171274652989725, 0.31506926682470227, 0.5268988094131738],
                 [0.8329609066098975, 0.3135561938839747, 0.31151129344017187, 0.5234945136135285],
                 [0.8300174457631608, 0.2852676708947365, 0.2831229867417112, 0.549039143174475],
                 [0.8455640805680781, 0.3082762947582698, 0.30616098851492407, 0.5415183982964997],
                 [0.8497856423001451, 0.3401630781673779, 0.33815669011961114, 0.5136353402283007],
                 [0.8499599690228088, 0.3427903034019835, 0.3407935724349724, 0.5111631275548476],
                 [0.8614852966013805, 0.3671670269861095, 0.3652208920663643, 0.49821053945476135],
                 [0.8677820295029943, 0.3553114594586141, 0.35329385878914804, 0.5165057713833123],
                 [0.8483797549082086, 0.34236899788405883, 0.34037682954931814, 0.5099950936936313],
                 [0.8578780804906609, 0.3453679580420141, 0.3433502016544211, 0.516545635223833],
                 [0.8476938881222286, 0.3543680539704557, 0.35242582627694485, 0.49721028953879465],
                 [0.8471941089994975, 0.3295763322821214, 0.32753846701945455, 0.5216935072427098],
                 [0.8284752307984489, 0.328511855751588, 0.326543496007309, 0.5039000945354188],
                 [0.8494419328612365, 0.3477862306194995, 0.3458112081697289, 0.5056057471412782],
                 [0.8435187505141456, 0.3385106805632099, 0.33652245981537154, 0.5089845114466124],
                 [0.8521381386998121, 0.3438553279887574, 0.34185421456076104, 0.5122850375670472],
                 [0.8551462804163964, 0.35331049905144946, 0.3513347676287528, 0.5057872442103402],
                 [0.8649389482440797, 0.3670739079651333, 0.3651138093813579, 0.5017852374464972],
                 [0.8524999580273603, 0.35208329188502296, 0.3501131475301319, 0.5043569548521195],
                 [0.8694108928504956, 0.3550838969369598, 0.3530589875042293, 0.5183768147789969],
                 [0.8404624821739002, 0.31402704787662883, 0.31195446742663957, 0.5305805951972498],
                 [0.8541816391689783, 0.3212060796477917, 0.31910775067329883, 0.5371722174701723],
                 [0.8337800485920621, 0.3142535547381249, 0.3122081748410621, 0.5236172536480627],
                 [0.8415078696205005, 0.30868543809898275, 0.3065877119906303, 0.5370178837382226],
                 [0.8429279063401268, 0.3034149715122197, 0.30129090483966886, 0.5437610681730087],
                 [0.8365685379168282, 0.3085618589384911, 0.3064830924858205, 0.5321642118836782],
                 [0.8525328259211619, 0.3106441216416888, 0.3085107015461004, 0.5461555444706501],
                 [0.8504957449068998, 0.2939696806295943, 0.29177863313243957, 0.560908159271615],
                 [0.8478648947494928, 0.3209967706076103, 0.3189224866542958, 0.5310166920485115],
                 [0.8464885656495535, 0.3207497207923371, 0.31867988282045834, 0.5298785208009742],
                 [0.8597741177157674, 0.34439878104569577, 0.3423697442871522, 0.5194334101871587],
                 [0.8633843882722556, 0.3371236318359559, 0.3350517390940807, 0.5304045419200503],
                 [0.8566465365996732, 0.3580180692143233, 0.3560549650120187, 0.5025546757899588],
                 [0.8471301989819916, 0.35137121466450427, 0.3494194076396322, 0.4996625983672313],
                 [0.8657179043383405, 0.35335016182833323, 0.3513329659916797, 0.5164021341833143],
                 [0.8574472788484435, 0.3615969984470655, 0.3596448319887924, 0.49975461331792426],
                 [0.8649786510294202, 0.3586158617073505, 0.35662230741868095, 0.5103498978994088],
                 [0.8708815660595557, 0.3537914399714981, 0.3517556520735136, 0.5211617018840267],
                 [0.8508121200050454, 0.3546405534430517, 0.3526871220786344, 0.5000784292908282],
                 [0.8501325185984505, 0.34259830204201014, 0.340600135835095, 0.5115305489702706],
                 [0.8501293296278687, 0.327398522273955, 0.325340526969412, 0.5268467979629996],
                 [0.8723016701645572, 0.35535406268773284, 0.353318835886643, 0.5210180610790041],
                 [0.8563949753871377, 0.34136050613804786, 0.3393328113772247, 0.5190898587707362],
                 [0.8602604006025223, 0.3722359715325715, 0.370314615512611, 0.4918671411098716]]

tex_fonts = {
    # Use LaTeX to write all text
    "text.usetex": True,
    "font.family": "serif",
    # Use 10pt font in plots, to match 10pt font in document
    "axes.labelsize": 16,
    "font.size": 12,
    # Make the legend/label fonts a little smaller
    "legend.fontsize": 12,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "axes.titlesize": 11
}

plt.rcParams.update(tex_fonts)

ax = plt.subplot(111)

fig, ax1 = plt.subplots()

batches = [i for i in range(len(eight_loss[:100]))]
ax1.plot(batches, eight_loss[:100], '-', markersize=4, mew=2, label='Loss')

ax2 = ax1.twinx()
next(ax2._get_lines.prop_cycler)['color']
ax2.plot(batches, [batch[3] for batch in eight_dhs_pos[:100]], '--', markersize=4, mew=2, label=r'$\bar{D}_{hs}$')

ax1.set_xlabel('Training batches', fontsize=14)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.set_ylim(5, 9.5)
ax2.set_ylim(0.15, 0.6)

fig.legend(loc='lower right')
ax1.grid(alpha=0.5)
# fig.savefig('../results/{}.pdf'.format(time.time()), dpi=3000, bbox_inches='tight')
fig.show()
