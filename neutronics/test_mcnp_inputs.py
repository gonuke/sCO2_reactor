from mcnp_inputs import HomogeneousInput, build_pyne_matlib

def test_homog_comp():
    """Test fuel, clad, coolant homogenization process.
    """
    exp_comp = {
        5010 : 4.36075073231383E-07,
        5011 : 1.92993563688806E-06,
        6012 : 0.001094775415103,
        6013 : 1.2830888245035E-05,
        7014 : 0.027662570472781,
        7015 : 0.000108256352761,
        8016 : 0.002851106,
        13027 : 0.000236598705025,
        14028 : 0.000138239891372,
        14029 : 7.2735173898753E-06,
        14030 : 4.96573362106248E-06,
        15031 : 6.62476374069704E-06,
        16032 : 6.27459765726019E-06,
        16033 : 5.10911243630757E-08,
        16034 : 2.98261059528482E-07,
        16036 : 7.43109212742188E-10,
        22046 : 3.3729984585759E-05,
        22047 : 3.10796058920701E-05,
        22048 : 0.000314491730693,
        22049 : 2.3560499046379E-05,
        22050 : 2.30182148144619E-05,
        24050 : 0.000375245546169,
        24052 : 0.007525258412022,
        24053 : 0.000869736839672,
        24054 : 0.000220576240721,
        25055 : 0.000150476776396,
        26054 : 0.000454146482321,
        26056 : 0.007392763137208,
        26057 : 0.000173786480815,
        26058 : 2.35335267940061E-05,
        27059 : 0.000430609643145,
        28058 : 0.016693931429147,
        28060 : 0.00665173599307,
        28061 : 0.000293978622968,
        28062 : 0.000952688345653,
        28064 : 0.000250425533347,
        29063 : 8.84642558088079E-05,
        29065 : 4.07195835296044E-05,
        41093 : 0.002425136726505,
        42092 : 0.000200848640696,
        42094 : 0.000129230212685,
        42095 : 0.000226098454496,
        42096 : 0.000240450531943,
        42097 : 0.000139919742178,
        42098 : 0.00035914737028,
        42100 : 0.000147557148376,
        74180 : 0.000527607417641,
        74182 : 0.117806570257708,
        74183 : 0.063967795288825,
        74184 : 0.137709758301018,
        74186 : 0.129170836958131,
        92235 : 0.424617184587787,
        92238 : 0.047179687176421
               }

    # build example input file
    matlib = build_pyne_matlib()
    obs = HomogeneousInput(15, 0.6, matlib)
    comp = obs.homog_core()
    obs_str = obs.fuel_string.split('\n')
    print('\n'.join(obs_str))
    
    # extract compositions from string
    for line in obs_str:
        if 'm' not in line and line != '':
            data = list(filter(None, line.split(' ')))
            print(data)
            assert abs(exp_comp[float(data[0])] - -float(data[1])) < 1e-5
