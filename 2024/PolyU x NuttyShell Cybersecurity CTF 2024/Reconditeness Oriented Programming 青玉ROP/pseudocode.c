#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define LODWORD(x) (*((unsigned int *)&(x)))

char const *const s = "?";
char const *const asc_42608E = ":)";
char const byte_426058 = 0x6E;
char const byte_426059 = 0x5;
char const byte_42605A = 0x0DF;
char const byte_42605B = 0x0A1;
char const byte_42605C = 0x0C6;
char const byte_42605D = 0x35;
char const byte_42605E = 0x34;
char const byte_42605F = 0x74;
char const byte_426060 = 0x3F;
char const byte_426061 = 0x92;
char const byte_426062 = 0x68;
char const byte_426063 = 0x36;
char const byte_426064 = 0x0B6;
char const byte_426065 = 0x58;
char const byte_426066 = 0x42;
char const byte_426067 = 0x33;
char const byte_426068 = 0x7B;
char const byte_426069 = 0x0EA;
char const byte_42606A = 0x6F;
char const byte_42606B = 0x0D6;
char const byte_42606C = 0x0F8;
char const byte_42606D = 0x7E;
char const byte_42606E = 0x9F;
char const byte_42606F = 0x0CC;
char const byte_426070 = 0x0A3;
char const byte_426071 = 0x0BF;
char const byte_426072 = 0x2;
char const byte_426073 = 0x0D3;
char const byte_426074 = 0x0F0;
char const byte_426075 = 0x0F9;
char const byte_426076 = 0x0A4;
char const byte_426077 = 0x22;
char const byte_426078 = 0x5F;
char const byte_426079 = 0x0C0;
char const byte_42607A = 0x0FA;
char const byte_42607B = 0x0;
char const byte_42607C = 0x1;
char const byte_42607D = 0x0;
char const byte_42607E = 0x65;
char const byte_42607F = 0x37;
char const byte_426080 = 0x10;
char const byte_426081 = 0x0F5;
char const byte_426082 = 0x0D7;
char const byte_426083 = 0x0D1;
char const byte_426084 = 0x0B9;
char const byte_426085 = 0x85;
char const byte_426086 = 0x8C;
char const byte_426087 = 0x0BC;
char const byte_426088 = 0x6E;
char const byte_426089 = 0x20;
char const byte_42608A = 0x70;
char const byte_42608B = 0x57;

void main()
{
  char *v0;   // rbx
  int v1;     // ebp
  int v2;     // eax
  char *v3;   // rdx
  char v4;    // r12
  char *v5;   // rbp
  int v6;     // eax
  char *v7;   // rdx
  char v8;    // r12
  char *v9;   // rbp
  int v10;    // eax
  char *v11;  // rdx
  char v12;   // r12
  char *v13;  // rbp
  int v14;    // eax
  char *v15;  // rdx
  char v16;   // r12
  char *v17;  // rbp
  int v18;    // eax
  char *v19;  // rdx
  char v20;   // r12
  char *v21;  // rbp
  int v22;    // eax
  char *v23;  // rdx
  char v24;   // r12
  char *v25;  // rbp
  int v26;    // eax
  char *v27;  // rdx
  char v28;   // r12
  char *v29;  // rbp
  int v30;    // eax
  char *v31;  // rdx
  char v32;   // r12
  char *v33;  // rbp
  int v34;    // eax
  char *v35;  // rdx
  char v36;   // r12
  char *v37;  // rbp
  int v38;    // eax
  char *v39;  // rdx
  char v40;   // r12
  char *v41;  // rbp
  int v42;    // eax
  char *v43;  // rdx
  char v44;   // r12
  char *v45;  // rbp
  int v46;    // eax
  char *v47;  // rdx
  char v48;   // r12
  char *v49;  // rbp
  int v50;    // eax
  char *v51;  // rdx
  char v52;   // r12
  char *v53;  // rbp
  int v54;    // eax
  char *v55;  // rdx
  char v56;   // r12
  char *v57;  // rbp
  int v58;    // eax
  char *v59;  // rdx
  char v60;   // r12
  char *v61;  // rbp
  int v62;    // eax
  char *v63;  // rdx
  char v64;   // r12
  char *v65;  // rbp
  int v66;    // eax
  char *v67;  // rdx
  char v68;   // r12
  char *v69;  // rbp
  int v70;    // eax
  char *v71;  // rdx
  char v72;   // r12
  char *v73;  // rbp
  int v74;    // eax
  char *v75;  // rdx
  char v76;   // r12
  char *v77;  // rbp
  int v78;    // eax
  char *v79;  // rdx
  char v80;   // r12
  char *v81;  // rbp
  int v82;    // eax
  char *v83;  // rdx
  char v84;   // r12
  char *v85;  // rbp
  int v86;    // eax
  char *v87;  // rdx
  char v88;   // r12
  char *v89;  // rbp
  int v90;    // eax
  char *v91;  // rdx
  char v92;   // r12
  char *v93;  // rbp
  int v94;    // eax
  char *v95;  // rdx
  char v96;   // r12
  char *v97;  // rbp
  int v98;    // eax
  char *v99;  // rdx
  char v100;  // r12
  char *v101; // rbp
  int v102;   // eax
  char *v103; // rdx
  char v104;  // r12
  char *v105; // rbp
  int v106;   // eax
  char *v107; // rdx
  char v108;  // r12
  char *v109; // rbp
  int v110;   // eax
  char *v111; // rdx
  char v112;  // r12
  char *v113; // rbp
  int v114;   // eax
  char *v115; // rdx
  char v116;  // r12
  char *v117; // rbp
  int v118;   // eax
  char *v119; // rdx
  char v120;  // r12
  char *v121; // rbp
  int v122;   // eax
  char *v123; // rdx
  char v124;  // r12
  char *v125; // rbp
  int v126;   // eax
  char *v127; // rdx
  char v128;  // r12
  char *v129; // rbp
  int v130;   // eax
  char *v131; // rdx
  char v132;  // r12
  char *v133; // rbp
  int v134;   // eax
  char *v135; // rdx
  char v136;  // r12
  char *v137; // rbp
  int v138;   // eax
  char *v139; // rdx
  char v140;  // r12
  char *v141; // rbp
  int v142;   // eax
  char *v143; // rdx
  char v144;  // r12
  char *v145; // rbp
  int v146;   // eax
  char *v147; // rdx
  char v148;  // r12
  char *v149; // rbp
  int v150;   // eax
  char *v151; // rdx
  char v152;  // r12
  char *v153; // rbp
  int v154;   // eax
  char *v155; // rdx
  char v156;  // r12
  char *v157; // rbp
  int v158;   // eax
  char *v159; // rdx
  char v160;  // r12
  char *v161; // rbp
  int v162;   // eax
  char *v163; // rdx
  char v164;  // r12
  char *v165; // rbp
  int v166;   // eax
  char *v167; // rdx
  char v168;  // r12
  char *v169; // rbp
  int v170;   // eax
  char *v171; // rdx
  char v172;  // r12
  char *v173; // rbp
  int v174;   // eax
  char *v175; // rdx
  char v176;  // r12
  char *v177; // rbp
  int v178;   // eax
  char *v179; // rdx
  char v180;  // r12
  char *v181; // rbp
  int v182;   // eax
  char *v183; // rdx
  char v184;  // r12
  char *v185; // rbp
  int v186;   // eax
  char *v187; // rdx
  char v188;  // r12
  char *v189; // rbp
  int v190;   // eax
  char *v191; // rdx
  char v192;  // r12
  char *v193; // rbp
  int v194;   // eax
  char *v195; // rdx
  char v196;  // r12
  char *v197; // rbp
  int v198;   // eax
  char *v199; // rdx
  char v200;  // r12
  char *v201; // rbp
  int v202;   // eax
  char *v203; // rdx
  char v204;  // r12
  char *v205; // rbp
  int v206;   // eax
  char *v207; // rdx
  char v208;  // r12
  char *v209; // rbp
  int v210;   // eax
  char *v211; // rdx
  char v212;  // r12
  char *v213; // rbp
  int v214;   // eax
  char *v215; // rdx
  char v216;  // r12
  char *v217; // rbp
  int v218;   // eax
  char *v219; // rdx
  char v220;  // r12
  char *v221; // rbp
  int v222;   // eax
  char *v223; // rdx
  char v224;  // r12
  char *v225; // rbp
  int v226;   // eax
  char *v227; // rdx
  char v228;  // r12
  char *v229; // rbp
  int v230;   // eax
  char *v231; // rdx
  char v232;  // r12
  char *v233; // rbp
  int v234;   // eax
  char *v235; // rdx
  char v236;  // r12
  char *v237; // rbp
  int v238;   // eax
  char *v239; // rdx
  char v240;  // r12
  char *v241; // rbp
  int v242;   // eax
  char *v243; // rdx
  char v244;  // r12
  char *v245; // rbp
  int v246;   // eax
  char *v247; // rdx
  char v248;  // r12
  char *v249; // rbp
  int v250;   // eax
  char *v251; // rdx
  char v252;  // r12
  char *v253; // rbp
  int v254;   // eax
  char *v255; // rdx
  char v256;  // r12
  char *v257; // rbp
  int v258;   // eax
  char *v259; // rdx
  char v260;  // r12
  char *v261; // rbp
  int v262;   // eax
  char *v263; // rdx
  char v264;  // r12
  char *v265; // rbp
  int v266;   // eax
  char *v267; // rdx
  char v268;  // r12
  char *v269; // rbp
  int v270;   // eax
  char *v271; // rdx
  char v272;  // r12
  char *v273; // rbp
  int v274;   // eax
  char *v275; // rdx
  char v276;  // r12
  char *v277; // rbp
  int v278;   // eax
  char *v279; // rdx
  char v280;  // r12
  char *v281; // rbp
  int v282;   // eax
  char *v283; // rdx
  char v284;  // r12
  char *v285; // rbp
  int v286;   // eax
  char *v287; // rdx
  char v288;  // r12
  char *v289; // rbp
  int v290;   // eax
  char *v291; // rdx
  char v292;  // r12
  char *v293; // rbp
  int v294;   // eax
  char *v295; // rdx
  char v296;  // r12
  char *v297; // rbp
  int v298;   // eax
  char *v299; // rdx
  char v300;  // r12
  char *v301; // rbp
  int v302;   // eax
  char *v303; // rdx
  char v304;  // r12
  char *v305; // rbp
  int v306;   // eax
  char *v307; // rdx
  char v308;  // r12
  char *v309; // rbp
  int v310;   // eax
  char *v311; // rdx
  char v312;  // r12
  char *v313; // rbp
  int v314;   // eax
  char *v315; // rdx
  char v316;  // r12
  char *v317; // rbp
  int v318;   // eax
  char *v319; // rdx
  char v320;  // r12
  char *v321; // rbp
  int v322;   // eax
  char *v323; // rdx
  char v324;  // r12
  char *v325; // rbp
  int v326;   // eax
  char *v327; // rdx
  char v328;  // r12
  char *v329; // rbp
  int v330;   // eax
  char *v331; // rdx
  char v332;  // r12
  char *v333; // rbp
  int v334;   // eax
  char *v335; // rdx
  char v336;  // r12
  char *v337; // rbp
  int v338;   // eax
  char *v339; // rdx
  char v340;  // r12
  char *v341; // rbp
  int v342;   // eax
  char *v343; // rdx
  char v344;  // r12
  char *v345; // rbp
  int v346;   // eax
  char *v347; // rdx
  char v348;  // r12
  char *v349; // rbp
  int v350;   // eax
  char *v351; // rdx
  char v352;  // r12
  char *v353; // rbp
  int v354;   // eax
  char *v355; // rdx
  char v356;  // r12
  char *v357; // rbp
  int v358;   // eax
  char *v359; // rdx
  char v360;  // r12
  char *v361; // rbp
  int v362;   // eax
  char *v363; // rdx
  char v364;  // r12
  char *v365; // rbp
  int v366;   // eax
  char *v367; // rdx
  char v368;  // r12
  char *v369; // rbp
  int v370;   // eax
  char *v371; // rdx
  char v372;  // r12
  char *v373; // rbp
  int v374;   // eax
  char *v375; // rdx
  char v376;  // r12
  char *v377; // rbp
  int v378;   // eax
  char *v379; // rdx
  char v380;  // r12
  char *v381; // rbp
  int v382;   // eax
  char *v383; // rdx
  char v384;  // r12
  char *v385; // rbp
  int v386;   // eax
  char *v387; // rdx
  char v388;  // r12
  char *v389; // rbp
  int v390;   // eax
  char *v391; // rdx
  char v392;  // r12
  char *v393; // rbp
  int v394;   // eax
  char *v395; // rdx
  char v396;  // r12
  char *v397; // rbp
  int v398;   // eax
  char *v399; // rdx
  char v400;  // r12
  char *v401; // rbp

  v0 = malloc(0x34uLL);
  srand(0x1D0u);
  puts(s);
  read(0, v0, 0x34uLL);
  v1 = rand();
  v2 = rand();
  v3 = &v0[v1 % 52];
  v4 = *v3;
  v5 = &v0[v2 % 52];
  *v3 = *v5;
  *v5 = rand() ^ v4;
  LODWORD(v5) = rand();
  v6 = rand();
  v7 = &v0[(int)v5 % 52];
  v8 = *v7;
  v9 = &v0[v6 % 52];
  *v7 = *v9;
  *v9 = rand() ^ v8;
  LODWORD(v9) = rand();
  v10 = rand();
  v11 = &v0[(int)v9 % 52];
  v12 = *v11;
  v13 = &v0[v10 % 52];
  *v11 = *v13;
  *v13 = rand() ^ v12;
  LODWORD(v13) = rand();
  v14 = rand();
  v15 = &v0[(int)v13 % 52];
  v16 = *v15;
  v17 = &v0[v14 % 52];
  *v15 = *v17;
  *v17 = rand() ^ v16;
  LODWORD(v17) = rand();
  v18 = rand();
  v19 = &v0[(int)v17 % 52];
  v20 = *v19;
  v21 = &v0[v18 % 52];
  *v19 = *v21;
  *v21 = rand() ^ v20;
  LODWORD(v21) = rand();
  v22 = rand();
  v23 = &v0[(int)v21 % 52];
  v24 = *v23;
  v25 = &v0[v22 % 52];
  *v23 = *v25;
  *v25 = rand() ^ v24;
  LODWORD(v25) = rand();
  v26 = rand();
  v27 = &v0[(int)v25 % 52];
  v28 = *v27;
  v29 = &v0[v26 % 52];
  *v27 = *v29;
  *v29 = rand() ^ v28;
  LODWORD(v29) = rand();
  v30 = rand();
  v31 = &v0[(int)v29 % 52];
  v32 = *v31;
  v33 = &v0[v30 % 52];
  *v31 = *v33;
  *v33 = rand() ^ v32;
  LODWORD(v33) = rand();
  v34 = rand();
  v35 = &v0[(int)v33 % 52];
  v36 = *v35;
  v37 = &v0[v34 % 52];
  *v35 = *v37;
  *v37 = rand() ^ v36;
  LODWORD(v37) = rand();
  v38 = rand();
  v39 = &v0[(int)v37 % 52];
  v40 = *v39;
  v41 = &v0[v38 % 52];
  *v39 = *v41;
  *v41 = rand() ^ v40;
  LODWORD(v41) = rand();
  v42 = rand();
  v43 = &v0[(int)v41 % 52];
  v44 = *v43;
  v45 = &v0[v42 % 52];
  *v43 = *v45;
  *v45 = rand() ^ v44;
  LODWORD(v45) = rand();
  v46 = rand();
  v47 = &v0[(int)v45 % 52];
  v48 = *v47;
  v49 = &v0[v46 % 52];
  *v47 = *v49;
  *v49 = rand() ^ v48;
  LODWORD(v49) = rand();
  v50 = rand();
  v51 = &v0[(int)v49 % 52];
  v52 = *v51;
  v53 = &v0[v50 % 52];
  *v51 = *v53;
  *v53 = rand() ^ v52;
  LODWORD(v53) = rand();
  v54 = rand();
  v55 = &v0[(int)v53 % 52];
  v56 = *v55;
  v57 = &v0[v54 % 52];
  *v55 = *v57;
  *v57 = rand() ^ v56;
  LODWORD(v57) = rand();
  v58 = rand();
  v59 = &v0[(int)v57 % 52];
  v60 = *v59;
  v61 = &v0[v58 % 52];
  *v59 = *v61;
  *v61 = rand() ^ v60;
  LODWORD(v61) = rand();
  v62 = rand();
  v63 = &v0[(int)v61 % 52];
  v64 = *v63;
  v65 = &v0[v62 % 52];
  *v63 = *v65;
  *v65 = rand() ^ v64;
  LODWORD(v65) = rand();
  v66 = rand();
  v67 = &v0[(int)v65 % 52];
  v68 = *v67;
  v69 = &v0[v66 % 52];
  *v67 = *v69;
  *v69 = rand() ^ v68;
  LODWORD(v69) = rand();
  v70 = rand();
  v71 = &v0[(int)v69 % 52];
  v72 = *v71;
  v73 = &v0[v70 % 52];
  *v71 = *v73;
  *v73 = rand() ^ v72;
  LODWORD(v73) = rand();
  v74 = rand();
  v75 = &v0[(int)v73 % 52];
  v76 = *v75;
  v77 = &v0[v74 % 52];
  *v75 = *v77;
  *v77 = rand() ^ v76;
  LODWORD(v77) = rand();
  v78 = rand();
  v79 = &v0[(int)v77 % 52];
  v80 = *v79;
  v81 = &v0[v78 % 52];
  *v79 = *v81;
  *v81 = rand() ^ v80;
  LODWORD(v81) = rand();
  v82 = rand();
  v83 = &v0[(int)v81 % 52];
  v84 = *v83;
  v85 = &v0[v82 % 52];
  *v83 = *v85;
  *v85 = rand() ^ v84;
  LODWORD(v85) = rand();
  v86 = rand();
  v87 = &v0[(int)v85 % 52];
  v88 = *v87;
  v89 = &v0[v86 % 52];
  *v87 = *v89;
  *v89 = rand() ^ v88;
  LODWORD(v89) = rand();
  v90 = rand();
  v91 = &v0[(int)v89 % 52];
  v92 = *v91;
  v93 = &v0[v90 % 52];
  *v91 = *v93;
  *v93 = rand() ^ v92;
  LODWORD(v93) = rand();
  v94 = rand();
  v95 = &v0[(int)v93 % 52];
  v96 = *v95;
  v97 = &v0[v94 % 52];
  *v95 = *v97;
  *v97 = rand() ^ v96;
  LODWORD(v97) = rand();
  v98 = rand();
  v99 = &v0[(int)v97 % 52];
  v100 = *v99;
  v101 = &v0[v98 % 52];
  *v99 = *v101;
  *v101 = rand() ^ v100;
  LODWORD(v101) = rand();
  v102 = rand();
  v103 = &v0[(int)v101 % 52];
  v104 = *v103;
  v105 = &v0[v102 % 52];
  *v103 = *v105;
  *v105 = rand() ^ v104;
  LODWORD(v105) = rand();
  v106 = rand();
  v107 = &v0[(int)v105 % 52];
  v108 = *v107;
  v109 = &v0[v106 % 52];
  *v107 = *v109;
  *v109 = rand() ^ v108;
  LODWORD(v109) = rand();
  v110 = rand();
  v111 = &v0[(int)v109 % 52];
  v112 = *v111;
  v113 = &v0[v110 % 52];
  *v111 = *v113;
  *v113 = rand() ^ v112;
  LODWORD(v113) = rand();
  v114 = rand();
  v115 = &v0[(int)v113 % 52];
  v116 = *v115;
  v117 = &v0[v114 % 52];
  *v115 = *v117;
  *v117 = rand() ^ v116;
  LODWORD(v117) = rand();
  v118 = rand();
  v119 = &v0[(int)v117 % 52];
  v120 = *v119;
  v121 = &v0[v118 % 52];
  *v119 = *v121;
  *v121 = rand() ^ v120;
  LODWORD(v121) = rand();
  v122 = rand();
  v123 = &v0[(int)v121 % 52];
  v124 = *v123;
  v125 = &v0[v122 % 52];
  *v123 = *v125;
  *v125 = rand() ^ v124;
  LODWORD(v125) = rand();
  v126 = rand();
  v127 = &v0[(int)v125 % 52];
  v128 = *v127;
  v129 = &v0[v126 % 52];
  *v127 = *v129;
  *v129 = rand() ^ v128;
  LODWORD(v129) = rand();
  v130 = rand();
  v131 = &v0[(int)v129 % 52];
  v132 = *v131;
  v133 = &v0[v130 % 52];
  *v131 = *v133;
  *v133 = rand() ^ v132;
  LODWORD(v133) = rand();
  v134 = rand();
  v135 = &v0[(int)v133 % 52];
  v136 = *v135;
  v137 = &v0[v134 % 52];
  *v135 = *v137;
  *v137 = rand() ^ v136;
  LODWORD(v137) = rand();
  v138 = rand();
  v139 = &v0[(int)v137 % 52];
  v140 = *v139;
  v141 = &v0[v138 % 52];
  *v139 = *v141;
  *v141 = rand() ^ v140;
  LODWORD(v141) = rand();
  v142 = rand();
  v143 = &v0[(int)v141 % 52];
  v144 = *v143;
  v145 = &v0[v142 % 52];
  *v143 = *v145;
  *v145 = rand() ^ v144;
  LODWORD(v145) = rand();
  v146 = rand();
  v147 = &v0[(int)v145 % 52];
  v148 = *v147;
  v149 = &v0[v146 % 52];
  *v147 = *v149;
  *v149 = rand() ^ v148;
  LODWORD(v149) = rand();
  v150 = rand();
  v151 = &v0[(int)v149 % 52];
  v152 = *v151;
  v153 = &v0[v150 % 52];
  *v151 = *v153;
  *v153 = rand() ^ v152;
  LODWORD(v153) = rand();
  v154 = rand();
  v155 = &v0[(int)v153 % 52];
  v156 = *v155;
  v157 = &v0[v154 % 52];
  *v155 = *v157;
  *v157 = rand() ^ v156;
  LODWORD(v157) = rand();
  v158 = rand();
  v159 = &v0[(int)v157 % 52];
  v160 = *v159;
  v161 = &v0[v158 % 52];
  *v159 = *v161;
  *v161 = rand() ^ v160;
  LODWORD(v161) = rand();
  v162 = rand();
  v163 = &v0[(int)v161 % 52];
  v164 = *v163;
  v165 = &v0[v162 % 52];
  *v163 = *v165;
  *v165 = rand() ^ v164;
  LODWORD(v165) = rand();
  v166 = rand();
  v167 = &v0[(int)v165 % 52];
  v168 = *v167;
  v169 = &v0[v166 % 52];
  *v167 = *v169;
  *v169 = rand() ^ v168;
  LODWORD(v169) = rand();
  v170 = rand();
  v171 = &v0[(int)v169 % 52];
  v172 = *v171;
  v173 = &v0[v170 % 52];
  *v171 = *v173;
  *v173 = rand() ^ v172;
  LODWORD(v173) = rand();
  v174 = rand();
  v175 = &v0[(int)v173 % 52];
  v176 = *v175;
  v177 = &v0[v174 % 52];
  *v175 = *v177;
  *v177 = rand() ^ v176;
  LODWORD(v177) = rand();
  v178 = rand();
  v179 = &v0[(int)v177 % 52];
  v180 = *v179;
  v181 = &v0[v178 % 52];
  *v179 = *v181;
  *v181 = rand() ^ v180;
  LODWORD(v181) = rand();
  v182 = rand();
  v183 = &v0[(int)v181 % 52];
  v184 = *v183;
  v185 = &v0[v182 % 52];
  *v183 = *v185;
  *v185 = rand() ^ v184;
  LODWORD(v185) = rand();
  v186 = rand();
  v187 = &v0[(int)v185 % 52];
  v188 = *v187;
  v189 = &v0[v186 % 52];
  *v187 = *v189;
  *v189 = rand() ^ v188;
  LODWORD(v189) = rand();
  v190 = rand();
  v191 = &v0[(int)v189 % 52];
  v192 = *v191;
  v193 = &v0[v190 % 52];
  *v191 = *v193;
  *v193 = rand() ^ v192;
  LODWORD(v193) = rand();
  v194 = rand();
  v195 = &v0[(int)v193 % 52];
  v196 = *v195;
  v197 = &v0[v194 % 52];
  *v195 = *v197;
  *v197 = rand() ^ v196;
  LODWORD(v197) = rand();
  v198 = rand();
  v199 = &v0[(int)v197 % 52];
  v200 = *v199;
  v201 = &v0[v198 % 52];
  *v199 = *v201;
  *v201 = rand() ^ v200;
  LODWORD(v201) = rand();
  v202 = rand();
  v203 = &v0[(int)v201 % 52];
  v204 = *v203;
  v205 = &v0[v202 % 52];
  *v203 = *v205;
  *v205 = rand() ^ v204;
  LODWORD(v205) = rand();
  v206 = rand();
  v207 = &v0[(int)v205 % 52];
  v208 = *v207;
  v209 = &v0[v206 % 52];
  *v207 = *v209;
  *v209 = rand() ^ v208;
  LODWORD(v209) = rand();
  v210 = rand();
  v211 = &v0[(int)v209 % 52];
  v212 = *v211;
  v213 = &v0[v210 % 52];
  *v211 = *v213;
  *v213 = rand() ^ v212;
  LODWORD(v213) = rand();
  v214 = rand();
  v215 = &v0[(int)v213 % 52];
  v216 = *v215;
  v217 = &v0[v214 % 52];
  *v215 = *v217;
  *v217 = rand() ^ v216;
  LODWORD(v217) = rand();
  v218 = rand();
  v219 = &v0[(int)v217 % 52];
  v220 = *v219;
  v221 = &v0[v218 % 52];
  *v219 = *v221;
  *v221 = rand() ^ v220;
  LODWORD(v221) = rand();
  v222 = rand();
  v223 = &v0[(int)v221 % 52];
  v224 = *v223;
  v225 = &v0[v222 % 52];
  *v223 = *v225;
  *v225 = rand() ^ v224;
  LODWORD(v225) = rand();
  v226 = rand();
  v227 = &v0[(int)v225 % 52];
  v228 = *v227;
  v229 = &v0[v226 % 52];
  *v227 = *v229;
  *v229 = rand() ^ v228;
  LODWORD(v229) = rand();
  v230 = rand();
  v231 = &v0[(int)v229 % 52];
  v232 = *v231;
  v233 = &v0[v230 % 52];
  *v231 = *v233;
  *v233 = rand() ^ v232;
  LODWORD(v233) = rand();
  v234 = rand();
  v235 = &v0[(int)v233 % 52];
  v236 = *v235;
  v237 = &v0[v234 % 52];
  *v235 = *v237;
  *v237 = rand() ^ v236;
  LODWORD(v237) = rand();
  v238 = rand();
  v239 = &v0[(int)v237 % 52];
  v240 = *v239;
  v241 = &v0[v238 % 52];
  *v239 = *v241;
  *v241 = rand() ^ v240;
  LODWORD(v241) = rand();
  v242 = rand();
  v243 = &v0[(int)v241 % 52];
  v244 = *v243;
  v245 = &v0[v242 % 52];
  *v243 = *v245;
  *v245 = rand() ^ v244;
  LODWORD(v245) = rand();
  v246 = rand();
  v247 = &v0[(int)v245 % 52];
  v248 = *v247;
  v249 = &v0[v246 % 52];
  *v247 = *v249;
  *v249 = rand() ^ v248;
  LODWORD(v249) = rand();
  v250 = rand();
  v251 = &v0[(int)v249 % 52];
  v252 = *v251;
  v253 = &v0[v250 % 52];
  *v251 = *v253;
  *v253 = rand() ^ v252;
  LODWORD(v253) = rand();
  v254 = rand();
  v255 = &v0[(int)v253 % 52];
  v256 = *v255;
  v257 = &v0[v254 % 52];
  *v255 = *v257;
  *v257 = rand() ^ v256;
  LODWORD(v257) = rand();
  v258 = rand();
  v259 = &v0[(int)v257 % 52];
  v260 = *v259;
  v261 = &v0[v258 % 52];
  *v259 = *v261;
  *v261 = rand() ^ v260;
  LODWORD(v261) = rand();
  v262 = rand();
  v263 = &v0[(int)v261 % 52];
  v264 = *v263;
  v265 = &v0[v262 % 52];
  *v263 = *v265;
  *v265 = rand() ^ v264;
  LODWORD(v265) = rand();
  v266 = rand();
  v267 = &v0[(int)v265 % 52];
  v268 = *v267;
  v269 = &v0[v266 % 52];
  *v267 = *v269;
  *v269 = rand() ^ v268;
  LODWORD(v269) = rand();
  v270 = rand();
  v271 = &v0[(int)v269 % 52];
  v272 = *v271;
  v273 = &v0[v270 % 52];
  *v271 = *v273;
  *v273 = rand() ^ v272;
  LODWORD(v273) = rand();
  v274 = rand();
  v275 = &v0[(int)v273 % 52];
  v276 = *v275;
  v277 = &v0[v274 % 52];
  *v275 = *v277;
  *v277 = rand() ^ v276;
  LODWORD(v277) = rand();
  v278 = rand();
  v279 = &v0[(int)v277 % 52];
  v280 = *v279;
  v281 = &v0[v278 % 52];
  *v279 = *v281;
  *v281 = rand() ^ v280;
  LODWORD(v281) = rand();
  v282 = rand();
  v283 = &v0[(int)v281 % 52];
  v284 = *v283;
  v285 = &v0[v282 % 52];
  *v283 = *v285;
  *v285 = rand() ^ v284;
  LODWORD(v285) = rand();
  v286 = rand();
  v287 = &v0[(int)v285 % 52];
  v288 = *v287;
  v289 = &v0[v286 % 52];
  *v287 = *v289;
  *v289 = rand() ^ v288;
  LODWORD(v289) = rand();
  v290 = rand();
  v291 = &v0[(int)v289 % 52];
  v292 = *v291;
  v293 = &v0[v290 % 52];
  *v291 = *v293;
  *v293 = rand() ^ v292;
  LODWORD(v293) = rand();
  v294 = rand();
  v295 = &v0[(int)v293 % 52];
  v296 = *v295;
  v297 = &v0[v294 % 52];
  *v295 = *v297;
  *v297 = rand() ^ v296;
  LODWORD(v297) = rand();
  v298 = rand();
  v299 = &v0[(int)v297 % 52];
  v300 = *v299;
  v301 = &v0[v298 % 52];
  *v299 = *v301;
  *v301 = rand() ^ v300;
  LODWORD(v301) = rand();
  v302 = rand();
  v303 = &v0[(int)v301 % 52];
  v304 = *v303;
  v305 = &v0[v302 % 52];
  *v303 = *v305;
  *v305 = rand() ^ v304;
  LODWORD(v305) = rand();
  v306 = rand();
  v307 = &v0[(int)v305 % 52];
  v308 = *v307;
  v309 = &v0[v306 % 52];
  *v307 = *v309;
  *v309 = rand() ^ v308;
  LODWORD(v309) = rand();
  v310 = rand();
  v311 = &v0[(int)v309 % 52];
  v312 = *v311;
  v313 = &v0[v310 % 52];
  *v311 = *v313;
  *v313 = rand() ^ v312;
  LODWORD(v313) = rand();
  v314 = rand();
  v315 = &v0[(int)v313 % 52];
  v316 = *v315;
  v317 = &v0[v314 % 52];
  *v315 = *v317;
  *v317 = rand() ^ v316;
  LODWORD(v317) = rand();
  v318 = rand();
  v319 = &v0[(int)v317 % 52];
  v320 = *v319;
  v321 = &v0[v318 % 52];
  *v319 = *v321;
  *v321 = rand() ^ v320;
  LODWORD(v321) = rand();
  v322 = rand();
  v323 = &v0[(int)v321 % 52];
  v324 = *v323;
  v325 = &v0[v322 % 52];
  *v323 = *v325;
  *v325 = rand() ^ v324;
  LODWORD(v325) = rand();
  v326 = rand();
  v327 = &v0[(int)v325 % 52];
  v328 = *v327;
  v329 = &v0[v326 % 52];
  *v327 = *v329;
  *v329 = rand() ^ v328;
  LODWORD(v329) = rand();
  v330 = rand();
  v331 = &v0[(int)v329 % 52];
  v332 = *v331;
  v333 = &v0[v330 % 52];
  *v331 = *v333;
  *v333 = rand() ^ v332;
  LODWORD(v333) = rand();
  v334 = rand();
  v335 = &v0[(int)v333 % 52];
  v336 = *v335;
  v337 = &v0[v334 % 52];
  *v335 = *v337;
  *v337 = rand() ^ v336;
  LODWORD(v337) = rand();
  v338 = rand();
  v339 = &v0[(int)v337 % 52];
  v340 = *v339;
  v341 = &v0[v338 % 52];
  *v339 = *v341;
  *v341 = rand() ^ v340;
  LODWORD(v341) = rand();
  v342 = rand();
  v343 = &v0[(int)v341 % 52];
  v344 = *v343;
  v345 = &v0[v342 % 52];
  *v343 = *v345;
  *v345 = rand() ^ v344;
  LODWORD(v345) = rand();
  v346 = rand();
  v347 = &v0[(int)v345 % 52];
  v348 = *v347;
  v349 = &v0[v346 % 52];
  *v347 = *v349;
  *v349 = rand() ^ v348;
  LODWORD(v349) = rand();
  v350 = rand();
  v351 = &v0[(int)v349 % 52];
  v352 = *v351;
  v353 = &v0[v350 % 52];
  *v351 = *v353;
  *v353 = rand() ^ v352;
  LODWORD(v353) = rand();
  v354 = rand();
  v355 = &v0[(int)v353 % 52];
  v356 = *v355;
  v357 = &v0[v354 % 52];
  *v355 = *v357;
  *v357 = rand() ^ v356;
  LODWORD(v357) = rand();
  v358 = rand();
  v359 = &v0[(int)v357 % 52];
  v360 = *v359;
  v361 = &v0[v358 % 52];
  *v359 = *v361;
  *v361 = rand() ^ v360;
  LODWORD(v361) = rand();
  v362 = rand();
  v363 = &v0[(int)v361 % 52];
  v364 = *v363;
  v365 = &v0[v362 % 52];
  *v363 = *v365;
  *v365 = rand() ^ v364;
  LODWORD(v365) = rand();
  v366 = rand();
  v367 = &v0[(int)v365 % 52];
  v368 = *v367;
  v369 = &v0[v366 % 52];
  *v367 = *v369;
  *v369 = rand() ^ v368;
  LODWORD(v369) = rand();
  v370 = rand();
  v371 = &v0[(int)v369 % 52];
  v372 = *v371;
  v373 = &v0[v370 % 52];
  *v371 = *v373;
  *v373 = rand() ^ v372;
  LODWORD(v373) = rand();
  v374 = rand();
  v375 = &v0[(int)v373 % 52];
  v376 = *v375;
  v377 = &v0[v374 % 52];
  *v375 = *v377;
  *v377 = rand() ^ v376;
  LODWORD(v377) = rand();
  v378 = rand();
  v379 = &v0[(int)v377 % 52];
  v380 = *v379;
  v381 = &v0[v378 % 52];
  *v379 = *v381;
  *v381 = rand() ^ v380;
  LODWORD(v381) = rand();
  v382 = rand();
  v383 = &v0[(int)v381 % 52];
  v384 = *v383;
  v385 = &v0[v382 % 52];
  *v383 = *v385;
  *v385 = rand() ^ v384;
  LODWORD(v385) = rand();
  v386 = rand();
  v387 = &v0[(int)v385 % 52];
  v388 = *v387;
  v389 = &v0[v386 % 52];
  *v387 = *v389;
  *v389 = rand() ^ v388;
  LODWORD(v389) = rand();
  v390 = rand();
  v391 = &v0[(int)v389 % 52];
  v392 = *v391;
  v393 = &v0[v390 % 52];
  *v391 = *v393;
  *v393 = rand() ^ v392;
  LODWORD(v393) = rand();
  v394 = rand();
  v395 = &v0[(int)v393 % 52];
  v396 = *v395;
  v397 = &v0[v394 % 52];
  *v395 = *v397;
  *v397 = rand() ^ v396;
  LODWORD(v397) = rand();
  v398 = rand();
  v399 = &v0[(int)v397 % 52];
  v400 = *v399;
  v401 = &v0[v398 % 52];
  *v399 = *v401;
  *v401 = rand() ^ v400;
  if (*v0 == byte_426058 && v0[1] == byte_426059 && v0[2] == byte_42605A && v0[3] == byte_42605B && v0[4] == byte_42605C && v0[5] == byte_42605D && v0[6] == byte_42605E && v0[7] == byte_42605F && v0[8] == byte_426060 && v0[9] == byte_426061 && v0[10] == byte_426062 && v0[11] == byte_426063 && v0[12] == byte_426064 && v0[13] == byte_426065 && v0[14] == byte_426066 && v0[15] == byte_426067 && v0[16] == byte_426068 && v0[17] == byte_426069 && v0[18] == byte_42606A && v0[19] == byte_42606B && v0[20] == byte_42606C && v0[21] == byte_42606D && v0[22] == byte_42606E && v0[23] == byte_42606F && v0[24] == byte_426070 && v0[25] == byte_426071 && v0[26] == byte_426072 && v0[27] == byte_426073 && v0[28] == byte_426074 && v0[29] == byte_426075 && v0[30] == byte_426076 && v0[31] == byte_426077 && v0[32] == byte_426078 && v0[33] == byte_426079 && v0[34] == byte_42607A && v0[35] == byte_42607B && v0[36] == byte_42607C && v0[37] == byte_42607D && v0[38] == byte_42607E && v0[39] == byte_42607F && v0[40] == byte_426080 && v0[41] == byte_426081 && v0[42] == byte_426082 && v0[43] == byte_426083 && v0[44] == byte_426084 && v0[45] == byte_426085 && v0[46] == byte_426086 && v0[47] == byte_426087 && v0[48] == byte_426088 && v0[49] == byte_426089 && v0[50] == byte_42608A && v0[51] == byte_42608B)
  {
    puts(asc_42608E);
    _exit(0);
  }
  _exit(-1);
}
