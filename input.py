database(
    thermoLibraries = ['primaryThermoLibrary']
)

species(
    label='1_vinyl',
    structure=adjacencyList(
        """
		1  C u0 p0 c0 {2,D} {6,S} {9,S}
		2  C u0 p0 c0 {1,D} {3,S} {10,S}
		3  C u0 p0 c0 {2,S} {4,D} {11,S}
		4  C u0 p0 c0 {3,D} {5,S} {12,S}
		5  C u0 p0 c0 {4,S} {6,D} {13,S}
		6  C u0 p0 c0 {1,S} {5,D} {7,S}
		7  C u0 p0 c0 {6,S} {8,D} {14,S}
		8  C u0 p0 c0 {7,D} {15,S} {16,S}
		9  H u0 p0 c0 {1,S}
		10 H u0 p0 c0 {2,S}
		11 H u0 p0 c0 {3,S}
		12 H u0 p0 c0 {4,S}
		13 H u0 p0 c0 {5,S}
		14 H u0 p0 c0 {7,S}
		15 H u0 p0 c0 {8,S}
		16 H u0 p0 c0 {8,S}
        """),
)

species(
    label='1_vinyl_2_vinyl_3CsCdOs',
    structure=adjacencyList(
        """
		1  C u0 p0 c0 {2,D} {12,S} {13,S}
		2  C u0 p0 c0 {1,D} {3,S} {14,S}
		3  C u0 p0 c0 {2,S} {4,S} {10,D}
		4  C u0 p0 c0 {3,S} {5,S} {7,D}
		5  C u0 p0 c0 {4,S} {6,D} {15,S}
		6  C u0 p0 c0 {5,D} {16,S} {17,S}
		7  C u0 p0 c0 {4,D} {8,S} {18,S}
		8  C u0 p0 c0 {7,S} {9,D} {19,S}
		9  C u0 p0 c0 {8,D} {10,S} {20,S}
		10 C u0 p0 c0 {3,D} {9,S} {11,S}
		11 C u0 p0 c0 {10,S} {21,S} {22,S} {23,S}
		12 H u0 p0 c0 {1,S}
		13 H u0 p0 c0 {1,S}
		14 H u0 p0 c0 {2,S}
		15 H u0 p0 c0 {5,S}
		16 H u0 p0 c0 {6,S}
		17 H u0 p0 c0 {6,S}
		18 H u0 p0 c0 {7,S}
		19 H u0 p0 c0 {8,S}
		20 H u0 p0 c0 {9,S}
		21 H u0 p0 c0 {11,S}
		22 H u0 p0 c0 {11,S}
		23 H u0 p0 c0 {11,S}
        """),
)

species(
    label='1_vinyl_2_formyl_3CsCdOs',
    structure=adjacencyList(
        """
		1  C u0 p0 c0 {2,D} {18,S} {19,S}
		2  C u0 p0 c0 {1,D} {3,S} {20,S}
		3  C u0 p0 c0 {2,S} {4,S} {16,D}
		4  C u0 p0 c0 {3,S} {5,S} {7,D}
		5  C u0 p0 c0 {4,S} {6,D} {21,S}
		6  C u0 p0 c0 {5,D} {22,S} {23,S}
		7  C u0 p0 c0 {4,D} {8,S} {10,S}
		8  C u0 p0 c0 {7,S} {9,D} {24,S}
		9  C u0 p0 c0 {8,D} {25,S} {26,S}
		10 C u0 p0 c0 {7,S} {11,S} {13,D}
		11 C u0 p0 c0 {10,S} {12,D} {27,S}
		12 O u0 p2 c0 {11,D}
		13 C u0 p0 c0 {10,D} {14,S} {16,S}
		14 C u0 p0 c0 {13,S} {15,D} {28,S}
		15 C u0 p0 c0 {14,D} {29,S} {30,S}
		16 C u0 p0 c0 {3,D} {13,S} {17,S}
		17 C u0 p0 c0 {16,S} {31,S} {32,S} {33,S}
		18 H u0 p0 c0 {1,S}
		19 H u0 p0 c0 {1,S}
		20 H u0 p0 c0 {2,S}
		21 H u0 p0 c0 {5,S}
		22 H u0 p0 c0 {6,S}
		23 H u0 p0 c0 {6,S}
		24 H u0 p0 c0 {8,S}
		25 H u0 p0 c0 {9,S}
		26 H u0 p0 c0 {9,S}
		27 H u0 p0 c0 {11,S}
		28 H u0 p0 c0 {14,S}
		29 H u0 p0 c0 {15,S}
		30 H u0 p0 c0 {15,S}
		31 H u0 p0 c0 {17,S}
		32 H u0 p0 c0 {17,S}
		33 H u0 p0 c0 {17,S}
        """),
)

species(
    label='123456methyl',
    structure=adjacencyList(
        """
		1 C u0 p0 c0 {2,D} {6,S} {7,S}
		2 C u0 p0 c0 {1,D} {3,S} {8,S}
		3 C u0 p0 c0 {2,S} {4,D} {9,S}
		4 C u0 p0 c0 {3,D} {5,S} {10,S}
		5 C u0 p0 c0 {4,S} {6,D} {11,S}
		6 C u0 p0 c0 {1,S} {5,D} {12,S}
		7 C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
		8 C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
		9 C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
		10 C u0 p0 c0 {4,S} {22,S} {23,S} {24,S}
		11 C u0 p0 c0 {5,S} {25,S} {26,S} {27,S}
		12 C u0 p0 c0 {6,S} {28,S} {29,S} {30,S}
		13 H u0 p0 c0 {7,S}
		14 H u0 p0 c0 {7,S}
		15 H u0 p0 c0 {7,S}
		16 H u0 p0 c0 {8,S}
		17 H u0 p0 c0 {8,S}
		18 H u0 p0 c0 {8,S}
		19 H u0 p0 c0 {9,S}
		20 H u0 p0 c0 {9,S}
		21 H u0 p0 c0 {9,S}
		22 H u0 p0 c0 {10,S}
		23 H u0 p0 c0 {10,S}
		24 H u0 p0 c0 {10,S}
		25 H u0 p0 c0 {11,S}
		26 H u0 p0 c0 {11,S}
		27 H u0 p0 c0 {11,S}
		28 H u0 p0 c0 {12,S}
		29 H u0 p0 c0 {12,S}
		30 H u0 p0 c0 {12,S}
        """),
)

species(
    label='123456ethyl',
    structure=adjacencyList(
        """
		1 C u0 p0 c0 {2,D} {6,S} {7,S}
		2 C u0 p0 c0 {1,D} {3,S} {8,S}
		3 C u0 p0 c0 {2,S} {4,D} {9,S}
		4 C u0 p0 c0 {3,D} {5,S} {10,S}
		5 C u0 p0 c0 {4,S} {6,D} {11,S}
		6 C u0 p0 c0 {1,S} {5,D} {12,S}
		7 C u0 p0 c0 {1,S} {13,S} {19,S} {20,S}
		8 C u0 p0 c0 {2,S} {14,S} {21,S} {22,S}
		9 C u0 p0 c0 {3,S} {15,S} {23,S} {24,S}
		10 C u0 p0 c0 {4,S} {16,S} {25,S} {26,S}
		11 C u0 p0 c0 {5,S} {17,S} {27,S} {28,S}
		12 C u0 p0 c0 {6,S} {18,S} {29,S} {30,S}
		13 C u0 p0 c0 {7,S} {31,S} {32,S} {33,S}
		14 C u0 p0 c0 {8,S} {34,S} {35,S} {36,S}
		15 C u0 p0 c0 {9,S} {37,S} {38,S} {39,S}
		16 C u0 p0 c0 {10,S} {40,S} {41,S} {42,S}
		17 C u0 p0 c0 {11,S} {43,S} {44,S} {45,S}
		18 C u0 p0 c0 {12,S} {46,S} {47,S} {48,S}
		19 H u0 p0 c0 {7,S}
		20 H u0 p0 c0 {7,S}
		21 H u0 p0 c0 {8,S}
		22 H u0 p0 c0 {8,S}
		23 H u0 p0 c0 {9,S}
		24 H u0 p0 c0 {9,S}
		25 H u0 p0 c0 {10,S}
		26 H u0 p0 c0 {10,S}
		27 H u0 p0 c0 {11,S}
		28 H u0 p0 c0 {11,S}
		29 H u0 p0 c0 {12,S}
		30 H u0 p0 c0 {12,S}
		31 H u0 p0 c0 {13,S}
		32 H u0 p0 c0 {13,S}
		33 H u0 p0 c0 {13,S}
		34 H u0 p0 c0 {14,S}
		35 H u0 p0 c0 {14,S}
		36 H u0 p0 c0 {14,S}
		37 H u0 p0 c0 {15,S}
		38 H u0 p0 c0 {15,S}
		39 H u0 p0 c0 {15,S}
		40 H u0 p0 c0 {16,S}
		41 H u0 p0 c0 {16,S}
		42 H u0 p0 c0 {16,S}
		43 H u0 p0 c0 {17,S}
		44 H u0 p0 c0 {17,S}
		45 H u0 p0 c0 {17,S}
		46 H u0 p0 c0 {18,S}
		47 H u0 p0 c0 {18,S}
		48 H u0 p0 c0 {18,S}
        """),
)

species(
    label='123ethyl_456vinyl',
    structure=adjacencyList(
        """
		1 C u0 p0 c0 {2,D} {3,S} {7,S}
		2 C u0 p0 c0 {1,D} {5,S} {8,S}
		3 C u0 p0 c0 {1,S} {4,D} {9,S}
		4 C u0 p0 c0 {3,D} {6,S} {13,S}
		5 C u0 p0 c0 {2,S} {6,D} {14,S}
		6 C u0 p0 c0 {4,S} {5,D} {15,S}
		7 C u0 p0 c0 {1,S} {10,S} {16,S} {17,S}
		8 C u0 p0 c0 {2,S} {11,S} {18,S} {19,S}
		9 C u0 p0 c0 {3,S} {12,S} {20,S} {21,S}
		10 C u0 p0 c0 {7,S} {25,S} {26,S} {27,S}
		11 C u0 p0 c0 {8,S} {28,S} {29,S} {30,S}
		12 C u0 p0 c0 {9,S} {31,S} {32,S} {33,S}
		13 C u0 p0 c0 {4,S} {22,D} {34,S}
		14 C u0 p0 c0 {5,S} {23,D} {35,S}
		15 C u0 p0 c0 {6,S} {24,D} {36,S}
		16 H u0 p0 c0 {7,S}
		17 H u0 p0 c0 {7,S}
		18 H u0 p0 c0 {8,S}
		19 H u0 p0 c0 {8,S}
		20 H u0 p0 c0 {9,S}
		21 H u0 p0 c0 {9,S}
		22 C u0 p0 c0 {13,D} {37,S} {38,S}
		23 C u0 p0 c0 {14,D} {39,S} {40,S}
		24 C u0 p0 c0 {15,D} {41,S} {42,S}
		25 H u0 p0 c0 {10,S}
		26 H u0 p0 c0 {10,S}
		27 H u0 p0 c0 {10,S}
		28 H u0 p0 c0 {11,S}
		29 H u0 p0 c0 {11,S}
		30 H u0 p0 c0 {11,S}
		31 H u0 p0 c0 {12,S}
		32 H u0 p0 c0 {12,S}
		33 H u0 p0 c0 {12,S}
		34 H u0 p0 c0 {13,S}
		35 H u0 p0 c0 {14,S}
		36 H u0 p0 c0 {15,S}
		37 H u0 p0 c0 {22,S}
		38 H u0 p0 c0 {22,S}
		39 H u0 p0 c0 {23,S}
		40 H u0 p0 c0 {23,S}
		41 H u0 p0 c0 {24,S}
		42 H u0 p0 c0 {24,S}
        """),
)

species(
    label='123456OH',
    structure=adjacencyList(
        """
		1 C u0 p0 c0 {2,D} {6,S} {7,S}
		2 C u0 p0 c0 {1,D} {3,S} {8,S}
		3 C u0 p0 c0 {2,S} {4,D} {9,S}
		4 C u0 p0 c0 {3,D} {5,S} {10,S}
		5 C u0 p0 c0 {4,S} {6,D} {11,S}
		6 C u0 p0 c0 {1,S} {5,D} {12,S}
		7 O u0 p2 c0 {1,S} {13,S}
		8 O u0 p2 c0 {2,S} {14,S}
		9 O u0 p2 c0 {3,S} {15,S}
		10 O u0 p2 c0 {4,S} {16,S}
		11 O u0 p2 c0 {5,S} {17,S}
		12 O u0 p2 c0 {6,S} {18,S}
		13 H u0 p0 c0 {7,S}
		14 H u0 p0 c0 {8,S}
		15 H u0 p0 c0 {9,S}
		16 H u0 p0 c0 {10,S}
		17 H u0 p0 c0 {11,S}
		18 H u0 p0 c0 {12,S}
        """),
)

species(
    label='1234OH_56methyl',
    structure=adjacencyList(
        """
		1 C u0 p0 c0 {2,D} {4,S} {7,S}
		2 C u0 p0 c0 {1,D} {3,S} {8,S}
		3 C u0 p0 c0 {2,S} {5,D} {9,S}
		4 C u0 p0 c0 {1,S} {6,D} {10,S}
		5 C u0 p0 c0 {3,D} {6,S} {11,S}
		6 C u0 p0 c0 {4,D} {5,S} {12,S}
		7 C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
		8 C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
		9 O u0 p2 c0 {3,S} {19,S}
		10 O u0 p2 c0 {4,S} {20,S}
		11 O u0 p2 c0 {5,S} {21,S}
		12 O u0 p2 c0 {6,S} {22,S}
		13 H u0 p0 c0 {7,S}
		14 H u0 p0 c0 {7,S}
		15 H u0 p0 c0 {7,S}
		16 H u0 p0 c0 {8,S}
		17 H u0 p0 c0 {8,S}
		18 H u0 p0 c0 {8,S}
		19 H u0 p0 c0 {9,S}
		20 H u0 p0 c0 {10,S}
		21 H u0 p0 c0 {11,S}
		22 H u0 p0 c0 {12,S}
        """),
)

species(
    label='12OH_34ethyl_56methyl',
    structure=adjacencyList(
        """
		1 C u0 p0 c0 {2,D} {3,S} {4,S}
		2 C u0 p0 c0 {1,D} {6,S} {7,S}
		3 C u0 p0 c0 {1,S} {5,D} {9,S}
		4 C u0 p0 c0 {1,S} {10,S} {15,S} {16,S}
		5 C u0 p0 c0 {3,D} {8,S} {12,S}
		6 C u0 p0 c0 {2,S} {11,S} {17,S} {18,S}
		7 C u0 p0 c0 {2,S} {8,D} {13,S}
		8 C u0 p0 c0 {5,S} {7,D} {14,S}
		9 C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
		10 C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
		11 C u0 p0 c0 {6,S} {28,S} {29,S} {30,S}
		12 C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
		13 O u0 p2 c0 {7,S} {31,S}
		14 O u0 p2 c0 {8,S} {32,S}
		15 H u0 p0 c0 {4,S}
		16 H u0 p0 c0 {4,S}
		17 H u0 p0 c0 {6,S}
		18 H u0 p0 c0 {6,S}
		19 H u0 p0 c0 {9,S}
		20 H u0 p0 c0 {9,S}
		21 H u0 p0 c0 {9,S}
		22 H u0 p0 c0 {12,S}
		23 H u0 p0 c0 {12,S}
		24 H u0 p0 c0 {12,S}
		25 H u0 p0 c0 {10,S}
		26 H u0 p0 c0 {10,S}
		27 H u0 p0 c0 {10,S}
		28 H u0 p0 c0 {11,S}
		29 H u0 p0 c0 {11,S}
		30 H u0 p0 c0 {11,S}
		31 H u0 p0 c0 {13,S}
		32 H u0 p0 c0 {14,S}
        """),
)

species(
    label='12OH_34vinyl_56methyl',
    structure=adjacencyList(
        """
		1 C u0 p0 c0 {2,S} {3,D} {7,S}
		2 C u0 p0 c0 {1,S} {4,D} {9,S}
		3 C u0 p0 c0 {1,D} {5,S} {8,S}
		4 C u0 p0 c0 {2,D} {6,S} {10,S}
		5 C u0 p0 c0 {3,S} {6,D} {12,S}
		6 C u0 p0 c0 {4,S} {5,D} {11,S}
		7 C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
		8 C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
		9 C u0 p0 c0 {2,S} {13,D} {21,S}
		10 C u0 p0 c0 {4,S} {14,D} {22,S}
		11 O u0 p2 c0 {6,S} {24,S}
		12 O u0 p2 c0 {5,S} {23,S}
		13 C u0 p0 c0 {9,D} {25,S} {26,S}
		14 C u0 p0 c0 {10,D} {27,S} {28,S}
		15 H u0 p0 c0 {7,S}
		16 H u0 p0 c0 {7,S}
		17 H u0 p0 c0 {7,S}
		18 H u0 p0 c0 {8,S}
		19 H u0 p0 c0 {8,S}
		20 H u0 p0 c0 {8,S}
		21 H u0 p0 c0 {9,S}
		22 H u0 p0 c0 {10,S}
		23 H u0 p0 c0 {12,S}
		24 H u0 p0 c0 {11,S}
		25 H u0 p0 c0 {13,S}
		26 H u0 p0 c0 {13,S}
		27 H u0 p0 c0 {14,S}
		28 H u0 p0 c0 {14,S}
        """),
)

species(
    label='testAromatics',
    structure=adjacencyList(
        """
		1  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
		2  O u0 p2 c0 {1,S} {3,S}
		3  C u0 p0 c0 {2,S} {4,D} {11,S}
		4  C u0 p0 c0 {3,D} {5,S} {16,S}
		5  C u0 p0 c0 {4,S} {6,S} {7,D}
		6  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
		7  C u0 p0 c0 {5,D} {8,S} {9,S}
		8  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
		9  C u0 p0 c0 {7,S} {10,S} {11,D}
		10 O u0 p2 c0 {9,S} {23,S}
		11 C u0 p0 c0 {3,S} {9,D} {12,S}
		12 O u0 p2 c0 {11,S} {24,S}
		13 H u0 p0 c0 {1,S}
		14 H u0 p0 c0 {1,S}
		15 H u0 p0 c0 {1,S}
		16 H u0 p0 c0 {4,S}
		17 H u0 p0 c0 {6,S}
		18 H u0 p0 c0 {6,S}
		19 H u0 p0 c0 {6,S}
		20 H u0 p0 c0 {8,S}
		21 H u0 p0 c0 {8,S}
		22 H u0 p0 c0 {8,S}
		23 H u0 p0 c0 {10,S}
		24 H u0 p0 c0 {12,S}
        """),
)
