from src.quantum.prf import generate_prf_byte_array

gen_prf_key1 = [-128, 53, 8, -15, -92, -21, -89, 117, -36, 93, 90, -21, 102, 29, -69, -108, -42, -120, -7, 78, -58, 19, 127, -62, 65, 72, 70, 45, 35, 37, 39, -8]
gen_prf_l1 = 192
gen_prf_nonce1 = 0
gen_prf_hash1 = [-72, 4, 0, 53, -66, -10, -92, -45, -40, 78, 32, 32, 17, 27, 44, 35, 86, 118, 102, 0, -72, 79, 72, -119, -40, -99, -107, -86, -50, -25, 41, 127, -27, -70, -79, 88, -81, 94, -62, 11, -26, -4, 32, -55, -27, -30, -34, -56, 81, 126, 101, 118, -56, -56, -31, -101, 82, -121, 65, 86, 33, 53, -21, -104, -27, 23, 122, -88, 68, -21, 66, -14, 49, 79, 12, -9, -60, -50, -45, 107, -8, -75, -108, 53, -125, 51, -103, 103, 85, 50, -117, -63, 23, -52, -104, -49, -11, -37, 34, -127, -42, 31, -18, 114, 94, -101, 125, 43, 110, -13, 52, 110, -91, 117, -4, 88, 34, 67, 118, 90, -105, 54, 91, 42, -84, -21, 42, -124, -125, 72, -122, 79, 81, 94, -123, -33, 63, 79, -71, 96, -17, -78, 1, -35, 54, 75, 105, 116, -40, -67, -100, -9, 7, 32, 16, 75, -27, -46, -118, 52, 31, -102, -115, 10, 67, 117, 38, 0, -24, 40, 13, 18, 81, -9, 79, 101, -18, -59, 63, -55, 43, -19, 11, -48, -85, -61, -3, -100, -65, 34, 32, 15]

assert(generate_prf_byte_array(gen_prf_l1, gen_prf_key1, gen_prf_nonce1) == gen_prf_hash1)

gen_prf_key2 = [-128, 53, 8, -15, -92, -21, -89, 117, -36, 93, 90, -21, 102, 29, -69, -108, -42, -120, -7, 78, -58, 19, 127, -62, 65, 72, 70, 45, 35, 37, 39, -8]
gen_prf_l2 = 128
gen_prf_nonce2 = 2
gen_prf_hash2 = [100, 70, -84, -86, 66, -46, -105, 3, 24, 13, 87, 17, 121, -43, 21, -113, -9, 110, -42, -45, -54, -27, 81, -61, 64, -11, 93, 69, 66, -71, -117, 61, 93, 26, 85, 22, -63, 27, 69, -110, 108, -71, 83, 54, 118, 91, 32, -95, -51, 57, -98, -26, 90, 62, -97, -22, -38, -87, 57, -65, 12, -16, 23, -98, 106, -109, -100, 85, 108, 55, 112, 4, 6, -87, 61, -26, -80, -55, 118, -58, -78, 126, 95, 112, -50, 61, 111, -14, 70, -83, 9, -77, 75, -118, -104, -49, -81, 63, -3, 14, -58, 55, 26, 75, 58, -76, 35, -106, 99, -105, 107, -65, 87, -58, 3, -34, -20, -53, 106, -33, 100, -61, -11, -126, -111, 3, -79, -76]

assert(generate_prf_byte_array(gen_prf_l2, gen_prf_key2, gen_prf_nonce2) == gen_prf_hash2)