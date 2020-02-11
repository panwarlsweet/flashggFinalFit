mgg[100,180];
Mjj[70,190];
mtot[200,1600];
ttHTagger[-1,1];
mgg_sig_m0_cat0[125., 122, 127];
mgg_sig_sigma_cat0[1.0, 0.1, 3.0];
mgg_sig_alpha1_cat0[1.0, 0.05, 10.0];
mgg_sig_n1_cat0[2.0, 0.1, 10.0];
mgg_sig_alpha2_cat0[1.0, 0.05, 10.0];
mgg_sig_n2_cat0[2.0, 0.1, 10.0];
mggSig_cat0 = RooDoubleCB(mgg, mgg_sig_m0_cat0, mgg_sig_sigma_cat0, mgg_sig_alpha1_cat0, mgg_sig_n1_cat0, mgg_sig_alpha2_cat0, mgg_sig_n2_cat0);

mgg_hig_m0_ggh_cat0[124.2, 123, 125];
mgg_hig_sigma_ggh_cat0[2.0, 0.1, 3.0];
mgg_hig_alpha1_ggh_cat0[1.0, 0.05, 10.0];
mgg_hig_n1_ggh_cat0[2.0, 0.1, 10.0];
mgg_hig_alpha2_ggh_cat0[1.0, 0.05, 10.0];
mgg_hig_n2_ggh_cat0[2.0, 0.1, 10.0];
mggHig_ggh_cat0 = RooDoubleCB(mgg, mgg_hig_m0_ggh_cat0, mgg_hig_sigma_ggh_cat0, mgg_hig_alpha1_ggh_cat0, mgg_hig_n1_ggh_cat0, mgg_hig_alpha2_ggh_cat0, mgg_hig_n2_ggh_cat0);

mgg_hig_m0_tth_cat0[124.2, 123, 125];
mgg_hig_sigma_tth_cat0[2.0, 0.1, 3.0];
mgg_hig_alpha1_tth_cat0[1.0, 0.05, 10.0];
mgg_hig_n1_tth_cat0[2.0, 0.1, 10.0];
mgg_hig_alpha2_tth_cat0[1.0, 0.05, 10.0];
mgg_hig_n2_tth_cat0[2.0, 0.1, 10.0];
mggHig_tth_cat0 = RooDoubleCB(mgg, mgg_hig_m0_tth_cat0, mgg_hig_sigma_tth_cat0, mgg_hig_alpha1_tth_cat0, mgg_hig_n1_tth_cat0, mgg_hig_alpha2_tth_cat0, mgg_hig_n2_tth_cat0);

mgg_hig_m0_vh_cat0[124.2, 123, 125];
mgg_hig_sigma_vh_cat0[2.0, 0.1, 3.0];
mgg_hig_alpha1_vh_cat0[1.0, 0.05, 10.0];
mgg_hig_n1_vh_cat0[2.0, 0.1, 10.0];
mgg_hig_alpha2_vh_cat0[1.0, 0.05, 10.0];
mgg_hig_n2_vh_cat0[2.0, 0.1, 10.0];
mggHig_vh_cat0 = RooDoubleCB(mgg, mgg_hig_m0_vh_cat0, mgg_hig_sigma_vh_cat0, mgg_hig_alpha1_vh_cat0, mgg_hig_n1_vh_cat0, mgg_hig_alpha2_vh_cat0, mgg_hig_n2_vh_cat0);

mgg_hig_m0_qqh_cat0[124.2, 123, 125];
mgg_hig_sigma_qqh_cat0[2.0, 0.1, 3.0];
mgg_hig_alpha1_qqh_cat0[1.0, 0.05, 10.0];
mgg_hig_n1_qqh_cat0[2.0, 0.1, 10.0];
mgg_hig_alpha2_qqh_cat0[1.0, 0.05, 10.0];
mgg_hig_n2_qqh_cat0[2.0, 0.1, 10.0];
mggHig_qqh_cat0 = RooDoubleCB(mgg, mgg_hig_m0_qqh_cat0, mgg_hig_sigma_qqh_cat0, mgg_hig_alpha1_qqh_cat0, mgg_hig_n1_qqh_cat0, mgg_hig_alpha2_qqh_cat0, mgg_hig_n2_qqh_cat0);

mgg_hig_m0_bbh_cat0[124.2, 123, 125];
mgg_hig_sigma_bbh_cat0[2.0, 0.1, 3.0];
mgg_hig_alpha1_bbh_cat0[1.0, 0.05, 10.0];
mgg_hig_n1_bbh_cat0[2.0, 0.1, 10.0];
mgg_hig_alpha2_bbh_cat0[1.0, 0.05, 10.0];
mgg_hig_n2_bbh_cat0[2.0, 0.1, 10.0];
mggHig_bbh_cat0 = RooDoubleCB(mgg, mgg_hig_m0_bbh_cat0, mgg_hig_sigma_bbh_cat0, mgg_hig_alpha1_bbh_cat0, mgg_hig_n1_bbh_cat0, mgg_hig_alpha2_bbh_cat0, mgg_hig_n2_bbh_cat0);


Mjj_sig_m0_cat0[110.0, 99, 140];
Mjj_sig_sigma_cat0[10.0, 1.0, 60.0];
Mjj_sig_alpha1_cat0[1.0, 0.05, 10.0];
Mjj_sig_n1_cat0[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat0[1.0, 0.05, 10.0];
Mjj_sig_n2_cat0[2.0, 0.1, 10.0];
MjjSig_cat0 = RooDoubleCB(Mjj, Mjj_sig_m0_cat0, Mjj_sig_sigma_cat0, Mjj_sig_alpha1_cat0, Mjj_sig_n1_cat0, Mjj_sig_alpha2_cat0, Mjj_sig_n2_cat0);

Mjj_hig_par1_ggh_cat0[0.1, 0, 10];
Mjj_hig_par2_ggh_cat0[0.1, 0, 10];
Mjj_hig_par3_ggh_cat0[0.1, 0, 10];

Mjj_hig_par1_qqh_cat0[0.1, 0, 10];
Mjj_hig_par2_qqh_cat0[0.1, 0, 10];
Mjj_hig_par3_qqh_cat0[0.1, 0, 10];

Mjj_hig_m0_tth_cat0[130, 70, 190];
Mjj_hig_sigma_tth_cat0[50, 10, 100];
Mjj_hig_alpha1_tth_cat0[1.0, 0.01, 10];
Mjj_hig_n1_tth_cat0[1, 0.01, 10];
Mjj_hig_alpha2_tth_cat0[1.0, 0.01, 10];
Mjj_hig_n2_tth_cat0[1, 0.01, 10];
MjjHig_tth_cat0 = RooDoubleCB(Mjj, Mjj_hig_m0_tth_cat0, Mjj_hig_sigma_tth_cat0, Mjj_hig_alpha1_tth_cat0, Mjj_hig_n1_tth_cat0, Mjj_hig_alpha2_tth_cat0, Mjj_hig_n2_tth_cat0);

Mjj_hig_m0_vh_cat0[90, 70, 190];
Mjj_hig_sigma_vh_cat0[50, 10, 100];
Mjj_hig_alpha1_vh_cat0[1.0, 0.01, 10];
Mjj_hig_n1_vh_cat0[1, 0.01, 10];
Mjj_hig_alpha2_vh_cat0[1.0, 0.01, 10];
Mjj_hig_n2_vh_cat0[1, 0.01, 10];
MjjHig_vh_cat0 = RooDoubleCB(Mjj, Mjj_hig_m0_vh_cat0, Mjj_hig_sigma_vh_cat0, Mjj_hig_alpha1_vh_cat0, Mjj_hig_n1_vh_cat0, Mjj_hig_alpha2_vh_cat0, Mjj_hig_n2_vh_cat0);

Mjj_hig_m0_bbh_cat0[100, 10, 180];
Mjj_hig_sigma_bbh_cat0[50, 1.0, 100];
Mjj_hig_alpha1_bbh_cat0[1.0, 0.01, 10];
Mjj_hig_n1_bbh_cat0[1, 0.01, 10];
Mjj_hig_alpha2_bbh_cat0[1.0, 0.01, 10];
Mjj_hig_n2_bbh_cat0[1, 0.01, 10];
MjjHig_bbh_cat0 = RooDoubleCB(Mjj, Mjj_hig_m0_bbh_cat0, Mjj_hig_sigma_bbh_cat0, Mjj_hig_alpha1_bbh_cat0, Mjj_hig_n1_bbh_cat0, Mjj_hig_alpha2_bbh_cat0, Mjj_hig_n2_bbh_cat0);
mgg_sig_m0_cat1[125., 122, 127];
mgg_sig_sigma_cat1[1.0, 0.1, 3.0];
mgg_sig_alpha1_cat1[1.0, 0.05, 10.0];
mgg_sig_n1_cat1[2.0, 0.1, 10.0];
mgg_sig_alpha2_cat1[1.0, 0.05, 10.0];
mgg_sig_n2_cat1[2.0, 0.1, 10.0];
mggSig_cat1 = RooDoubleCB(mgg, mgg_sig_m0_cat1, mgg_sig_sigma_cat1, mgg_sig_alpha1_cat1, mgg_sig_n1_cat1, mgg_sig_alpha2_cat1, mgg_sig_n2_cat1);

mgg_hig_m0_ggh_cat1[124.2, 123, 125];
mgg_hig_sigma_ggh_cat1[2.0, 0.1, 3.0];
mgg_hig_alpha1_ggh_cat1[1.0, 0.05, 10.0];
mgg_hig_n1_ggh_cat1[2.0, 0.1, 10.0];
mgg_hig_alpha2_ggh_cat1[1.0, 0.05, 10.0];
mgg_hig_n2_ggh_cat1[2.0, 0.1, 10.0];
mggHig_ggh_cat1 = RooDoubleCB(mgg, mgg_hig_m0_ggh_cat1, mgg_hig_sigma_ggh_cat1, mgg_hig_alpha1_ggh_cat1, mgg_hig_n1_ggh_cat1, mgg_hig_alpha2_ggh_cat1, mgg_hig_n2_ggh_cat1);

mgg_hig_m0_tth_cat1[124.2, 123, 125];
mgg_hig_sigma_tth_cat1[2.0, 0.1, 3.0];
mgg_hig_alpha1_tth_cat1[1.0, 0.05, 10.0];
mgg_hig_n1_tth_cat1[2.0, 0.1, 10.0];
mgg_hig_alpha2_tth_cat1[1.0, 0.05, 10.0];
mgg_hig_n2_tth_cat1[2.0, 0.1, 10.0];
mggHig_tth_cat1 = RooDoubleCB(mgg, mgg_hig_m0_tth_cat1, mgg_hig_sigma_tth_cat1, mgg_hig_alpha1_tth_cat1, mgg_hig_n1_tth_cat1, mgg_hig_alpha2_tth_cat1, mgg_hig_n2_tth_cat1);

mgg_hig_m0_vh_cat1[124.2, 123, 125];
mgg_hig_sigma_vh_cat1[2.0, 0.1, 3.0];
mgg_hig_alpha1_vh_cat1[1.0, 0.05, 10.0];
mgg_hig_n1_vh_cat1[2.0, 0.1, 10.0];
mgg_hig_alpha2_vh_cat1[1.0, 0.05, 10.0];
mgg_hig_n2_vh_cat1[2.0, 0.1, 10.0];
mggHig_vh_cat1 = RooDoubleCB(mgg, mgg_hig_m0_vh_cat1, mgg_hig_sigma_vh_cat1, mgg_hig_alpha1_vh_cat1, mgg_hig_n1_vh_cat1, mgg_hig_alpha2_vh_cat1, mgg_hig_n2_vh_cat1);

mgg_hig_m0_qqh_cat1[124.2, 123, 125];
mgg_hig_sigma_qqh_cat1[2.0, 0.1, 3.0];
mgg_hig_alpha1_qqh_cat1[1.0, 0.05, 10.0];
mgg_hig_n1_qqh_cat1[2.0, 0.1, 10.0];
mgg_hig_alpha2_qqh_cat1[1.0, 0.05, 10.0];
mgg_hig_n2_qqh_cat1[2.0, 0.1, 10.0];
mggHig_qqh_cat1 = RooDoubleCB(mgg, mgg_hig_m0_qqh_cat1, mgg_hig_sigma_qqh_cat1, mgg_hig_alpha1_qqh_cat1, mgg_hig_n1_qqh_cat1, mgg_hig_alpha2_qqh_cat1, mgg_hig_n2_qqh_cat1);

mgg_hig_m0_bbh_cat1[124.2, 123, 125];
mgg_hig_sigma_bbh_cat1[2.0, 0.1, 3.0];
mgg_hig_alpha1_bbh_cat1[1.0, 0.05, 10.0];
mgg_hig_n1_bbh_cat1[2.0, 0.1, 10.0];
mgg_hig_alpha2_bbh_cat1[1.0, 0.05, 10.0];
mgg_hig_n2_bbh_cat1[2.0, 0.1, 10.0];
mggHig_bbh_cat1 = RooDoubleCB(mgg, mgg_hig_m0_bbh_cat1, mgg_hig_sigma_bbh_cat1, mgg_hig_alpha1_bbh_cat1, mgg_hig_n1_bbh_cat1, mgg_hig_alpha2_bbh_cat1, mgg_hig_n2_bbh_cat1);


Mjj_sig_m0_cat1[110.0, 99, 140];
Mjj_sig_sigma_cat1[10.0, 1.0, 60.0];
Mjj_sig_alpha1_cat1[1.0, 0.05, 10.0];
Mjj_sig_n1_cat1[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat1[1.0, 0.05, 10.0];
Mjj_sig_n2_cat1[2.0, 0.1, 5.0];
MjjSig_cat1 = RooDoubleCB(Mjj, Mjj_sig_m0_cat1, Mjj_sig_sigma_cat1, Mjj_sig_alpha1_cat1, Mjj_sig_n1_cat1, Mjj_sig_alpha2_cat1, Mjj_sig_n2_cat1);

Mjj_hig_par1_ggh_cat1[0.1, 0, 10];
Mjj_hig_par2_ggh_cat1[0.1, 0, 10];
Mjj_hig_par3_ggh_cat1[0.1, 0, 10];

Mjj_hig_par1_qqh_cat1[0.1, 0, 10];
Mjj_hig_par2_qqh_cat1[0.1, 0, 10];
Mjj_hig_par3_qqh_cat1[0.1, 0, 10];

Mjj_hig_m0_tth_cat1[130, 70, 190];
Mjj_hig_sigma_tth_cat1[50, 10, 100];
Mjj_hig_alpha1_tth_cat1[1.0, 0.01, 10];
Mjj_hig_n1_tth_cat1[1, 0.01, 10];
Mjj_hig_alpha2_tth_cat1[1.0, 0.01, 10];
Mjj_hig_n2_tth_cat1[1, 0.01, 10];
MjjHig_tth_cat1 = RooDoubleCB(Mjj, Mjj_hig_m0_tth_cat1, Mjj_hig_sigma_tth_cat1, Mjj_hig_alpha1_tth_cat1, Mjj_hig_n1_tth_cat1, Mjj_hig_alpha2_tth_cat1, Mjj_hig_n2_tth_cat1);

Mjj_hig_m0_vh_cat1[90, 70, 190];
Mjj_hig_sigma_vh_cat1[50, 10, 100];
Mjj_hig_alpha1_vh_cat1[1.0, 0.01, 10];
Mjj_hig_n1_vh_cat1[1, 0.01, 10];
Mjj_hig_alpha2_vh_cat1[1.0, 0.01, 10];
Mjj_hig_n2_vh_cat1[1, 0.01, 10];
MjjHig_vh_cat1 = RooDoubleCB(Mjj, Mjj_hig_m0_vh_cat1, Mjj_hig_sigma_vh_cat1, Mjj_hig_alpha1_vh_cat1, Mjj_hig_n1_vh_cat1, Mjj_hig_alpha2_vh_cat1, Mjj_hig_n2_vh_cat1);

Mjj_hig_m0_bbh_cat1[100, 10, 180];
Mjj_hig_sigma_bbh_cat1[50, 1.0, 100];
Mjj_hig_alpha1_bbh_cat1[1.0, 0.01, 10];
Mjj_hig_n1_bbh_cat1[1, 0.01, 10];
Mjj_hig_alpha2_bbh_cat1[1.0, 0.01, 10];
Mjj_hig_n2_bbh_cat1[1, 0.01, 10];
MjjHig_bbh_cat1 = RooDoubleCB(Mjj, Mjj_hig_m0_bbh_cat1, Mjj_hig_sigma_bbh_cat1, Mjj_hig_alpha1_bbh_cat1, Mjj_hig_n1_bbh_cat1, Mjj_hig_alpha2_bbh_cat1, Mjj_hig_n2_bbh_cat1);
mgg_sig_m0_cat10[125., 122, 127];
mgg_sig_sigma_cat10[1.0, 0.1, 3.0];
mgg_sig_alpha1_cat10[1.0, 0.05, 10.0];
mgg_sig_n1_cat10[2.0, 0.1, 10.0];
mgg_sig_alpha2_cat10[1.0, 0.05, 10.0];
mgg_sig_n2_cat10[2.0, 0.1, 10.0];
mggSig_cat10 = RooDoubleCB(mgg, mgg_sig_m0_cat10, mgg_sig_sigma_cat10, mgg_sig_alpha1_cat10, mgg_sig_n1_cat10, mgg_sig_alpha2_cat10, mgg_sig_n2_cat10);

mgg_hig_m0_ggh_cat10[124.2, 123, 125];
mgg_hig_sigma_ggh_cat10[2.0, 0.1, 3.0];
mgg_hig_alpha1_ggh_cat10[1.0, 0.05, 10.0];
mgg_hig_n1_ggh_cat10[2.0, 0.1, 10.0];
mgg_hig_alpha2_ggh_cat10[1.0, 0.05, 10.0];
mgg_hig_n2_ggh_cat10[2.0, 0.1, 10.0];
mggHig_ggh_cat10 = RooDoubleCB(mgg, mgg_hig_m0_ggh_cat10, mgg_hig_sigma_ggh_cat10, mgg_hig_alpha1_ggh_cat10, mgg_hig_n1_ggh_cat10, mgg_hig_alpha2_ggh_cat10, mgg_hig_n2_ggh_cat10);

mgg_hig_m0_tth_cat10[124.2, 123, 125];
mgg_hig_sigma_tth_cat10[2.0, 0.1, 3.0];
mgg_hig_alpha1_tth_cat10[1.0, 0.05, 10.0];
mgg_hig_n1_tth_cat10[2.0, 0.1, 10.0];
mgg_hig_alpha2_tth_cat10[1.0, 0.05, 10.0];
mgg_hig_n2_tth_cat10[2.0, 0.1, 10.0];
mggHig_tth_cat10 = RooDoubleCB(mgg, mgg_hig_m0_tth_cat10, mgg_hig_sigma_tth_cat10, mgg_hig_alpha1_tth_cat10, mgg_hig_n1_tth_cat10, mgg_hig_alpha2_tth_cat10, mgg_hig_n2_tth_cat10);

mgg_hig_m0_vh_cat10[124.2, 123, 125];
mgg_hig_sigma_vh_cat10[2.0, 0.1, 3.0];
mgg_hig_alpha1_vh_cat10[1.0, 0.05, 10.0];
mgg_hig_n1_vh_cat10[2.0, 0.1, 10.0];
mgg_hig_alpha2_vh_cat10[1.0, 0.05, 10.0];
mgg_hig_n2_vh_cat10[2.0, 0.1, 10.0];
mggHig_vh_cat10 = RooDoubleCB(mgg, mgg_hig_m0_vh_cat10, mgg_hig_sigma_vh_cat10, mgg_hig_alpha1_vh_cat10, mgg_hig_n1_vh_cat10, mgg_hig_alpha2_vh_cat10, mgg_hig_n2_vh_cat10);

mgg_hig_m0_qqh_cat10[124.2, 123, 125];
mgg_hig_sigma_qqh_cat10[2.0, 0.1, 3.0];
mgg_hig_alpha1_qqh_cat10[1.0, 0.05, 10.0];
mgg_hig_n1_qqh_cat10[2.0, 0.1, 10.0];
mgg_hig_alpha2_qqh_cat10[1.0, 0.05, 10.0];
mgg_hig_n2_qqh_cat10[2.0, 0.1, 10.0];
mggHig_qqh_cat10 = RooDoubleCB(mgg, mgg_hig_m0_qqh_cat10, mgg_hig_sigma_qqh_cat10, mgg_hig_alpha1_qqh_cat10, mgg_hig_n1_qqh_cat10, mgg_hig_alpha2_qqh_cat10, mgg_hig_n2_qqh_cat10);

mgg_hig_m0_bbh_cat10[124.2, 123, 125];
mgg_hig_sigma_bbh_cat10[2.0, 0.1, 3.0];
mgg_hig_alpha1_bbh_cat10[1.0, 0.05, 10.0];
mgg_hig_n1_bbh_cat10[2.0, 0.1, 10.0];
mgg_hig_alpha2_bbh_cat10[1.0, 0.05, 10.0];
mgg_hig_n2_bbh_cat10[2.0, 0.1, 10.0];
mggHig_bbh_cat10 = RooDoubleCB(mgg, mgg_hig_m0_bbh_cat10, mgg_hig_sigma_bbh_cat10, mgg_hig_alpha1_bbh_cat10, mgg_hig_n1_bbh_cat10, mgg_hig_alpha2_bbh_cat10, mgg_hig_n2_bbh_cat10);


Mjj_sig_m0_cat10[110.0, 99, 140];
Mjj_sig_sigma_cat10[20.0, 1.0, 60.0];
Mjj_sig_alpha1_cat10[1.0, 0.05, 10.0];
Mjj_sig_n1_cat10[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat10[1.0, 0.05, 10.0];
Mjj_sig_n2_cat10[2.0, 0.1, 10.0];
MjjSig_cat10 = RooDoubleCB(Mjj, Mjj_sig_m0_cat10, Mjj_sig_sigma_cat10, Mjj_sig_alpha1_cat10, Mjj_sig_n1_cat10, Mjj_sig_alpha2_cat10, Mjj_sig_n2_cat10);

Mjj_hig_par1_ggh_cat10[0.1, 0, 10];
Mjj_hig_par2_ggh_cat10[0.1, 0, 10];
Mjj_hig_par3_ggh_cat10[0.1, 0, 10];

Mjj_hig_par1_qqh_cat10[0.1, 0, 10];
Mjj_hig_par2_qqh_cat10[0.1, 0, 10];
Mjj_hig_par3_qqh_cat10[0.1, 0, 10];

Mjj_hig_m0_tth_cat10[130, 70, 190];
Mjj_hig_sigma_tth_cat10[50, 10, 100];
Mjj_hig_alpha1_tth_cat10[1.0, 0.01, 10];
Mjj_hig_n1_tth_cat10[1, 0.01, 10];
Mjj_hig_alpha2_tth_cat10[1.0, 0.01, 10];
Mjj_hig_n2_tth_cat10[1, 0.01, 10];
MjjHig_tth_cat10 = RooDoubleCB(Mjj, Mjj_hig_m0_tth_cat10, Mjj_hig_sigma_tth_cat10, Mjj_hig_alpha1_tth_cat10, Mjj_hig_n1_tth_cat10, Mjj_hig_alpha2_tth_cat10, Mjj_hig_n2_tth_cat10);

Mjj_hig_m0_vh_cat10[90, 70, 190];
Mjj_hig_sigma_vh_cat10[50, 10, 100];
Mjj_hig_alpha1_vh_cat10[1.0, 0.01, 10];
Mjj_hig_n1_vh_cat10[1, 0.01, 10];
Mjj_hig_alpha2_vh_cat10[1.0, 0.01, 10];
Mjj_hig_n2_vh_cat10[1, 0.01, 10];
MjjHig_vh_cat10 = RooDoubleCB(Mjj, Mjj_hig_m0_vh_cat10, Mjj_hig_sigma_vh_cat10, Mjj_hig_alpha1_vh_cat10, Mjj_hig_n1_vh_cat10, Mjj_hig_alpha2_vh_cat10, Mjj_hig_n2_vh_cat10);

Mjj_hig_m0_bbh_cat10[100, 10, 180];
Mjj_hig_sigma_bbh_cat10[50, 1.0, 100];
Mjj_hig_alpha1_bbh_cat10[1.0, 0.01, 10];
Mjj_hig_n1_bbh_cat10[1, 0.01, 10];
Mjj_hig_alpha2_bbh_cat10[1.0, 0.01, 10];
Mjj_hig_n2_bbh_cat10[1, 0.01, 10];
MjjHig_bbh_cat10 = RooDoubleCB(Mjj, Mjj_hig_m0_bbh_cat10, Mjj_hig_sigma_bbh_cat10, Mjj_hig_alpha1_bbh_cat10, Mjj_hig_n1_bbh_cat10, Mjj_hig_alpha2_bbh_cat10, Mjj_hig_n2_bbh_cat10);
mgg_sig_m0_cat11[125., 122, 127];
mgg_sig_sigma_cat11[1.0, 0.1, 3.0];
mgg_sig_alpha1_cat11[1.0, 0.05, 10.0];
mgg_sig_n1_cat11[2.0, 0.1, 10.0];
mgg_sig_alpha2_cat11[1.0, 0.05, 10.0];
mgg_sig_n2_cat11[2.0, 0.1, 10.0];
mggSig_cat11 = RooDoubleCB(mgg, mgg_sig_m0_cat11, mgg_sig_sigma_cat11, mgg_sig_alpha1_cat11, mgg_sig_n1_cat11, mgg_sig_alpha2_cat11, mgg_sig_n2_cat11);

mgg_hig_m0_ggh_cat11[124.2, 123, 125];
mgg_hig_sigma_ggh_cat11[2.0, 0.1, 3.0];
mgg_hig_alpha1_ggh_cat11[1.0, 0.05, 10.0];
mgg_hig_n1_ggh_cat11[2.0, 0.1, 10.0];
mgg_hig_alpha2_ggh_cat11[1.0, 0.05, 10.0];
mgg_hig_n2_ggh_cat11[2.0, 0.1, 10.0];
mggHig_ggh_cat11 = RooDoubleCB(mgg, mgg_hig_m0_ggh_cat11, mgg_hig_sigma_ggh_cat11, mgg_hig_alpha1_ggh_cat11, mgg_hig_n1_ggh_cat11, mgg_hig_alpha2_ggh_cat11, mgg_hig_n2_ggh_cat11);

mgg_hig_m0_tth_cat11[124.2, 123, 125];
mgg_hig_sigma_tth_cat11[2.0, 0.1, 3.0];
mgg_hig_alpha1_tth_cat11[1.0, 0.05, 10.0];
mgg_hig_n1_tth_cat11[2.0, 0.1, 10.0];
mgg_hig_alpha2_tth_cat11[1.0, 0.05, 10.0];
mgg_hig_n2_tth_cat11[2.0, 0.1, 10.0];
mggHig_tth_cat11 = RooDoubleCB(mgg, mgg_hig_m0_tth_cat11, mgg_hig_sigma_tth_cat11, mgg_hig_alpha1_tth_cat11, mgg_hig_n1_tth_cat11, mgg_hig_alpha2_tth_cat11, mgg_hig_n2_tth_cat11);

mgg_hig_m0_vh_cat11[124.2, 123, 125];
mgg_hig_sigma_vh_cat11[2.0, 0.1, 3.0];
mgg_hig_alpha1_vh_cat11[1.0, 0.05, 10.0];
mgg_hig_n1_vh_cat11[2.0, 0.1, 10.0];
mgg_hig_alpha2_vh_cat11[1.0, 0.05, 10.0];
mgg_hig_n2_vh_cat11[2.0, 0.1, 10.0];
mggHig_vh_cat11 = RooDoubleCB(mgg, mgg_hig_m0_vh_cat11, mgg_hig_sigma_vh_cat11, mgg_hig_alpha1_vh_cat11, mgg_hig_n1_vh_cat11, mgg_hig_alpha2_vh_cat11, mgg_hig_n2_vh_cat11);

mgg_hig_m0_qqh_cat11[124.2, 123, 125];
mgg_hig_sigma_qqh_cat11[2.0, 0.1, 3.0];
mgg_hig_alpha1_qqh_cat11[1.0, 0.05, 10.0];
mgg_hig_n1_qqh_cat11[2.0, 0.1, 10.0];
mgg_hig_alpha2_qqh_cat11[1.0, 0.05, 10.0];
mgg_hig_n2_qqh_cat11[2.0, 0.1, 10.0];
mggHig_qqh_cat11 = RooDoubleCB(mgg, mgg_hig_m0_qqh_cat11, mgg_hig_sigma_qqh_cat11, mgg_hig_alpha1_qqh_cat11, mgg_hig_n1_qqh_cat11, mgg_hig_alpha2_qqh_cat11, mgg_hig_n2_qqh_cat11);

mgg_hig_m0_bbh_cat11[124.2, 123, 125];
mgg_hig_sigma_bbh_cat11[2.0, 0.1, 3.0];
mgg_hig_alpha1_bbh_cat11[1.0, 0.05, 10.0];
mgg_hig_n1_bbh_cat11[2.0, 0.1, 10.0];
mgg_hig_alpha2_bbh_cat11[1.0, 0.05, 10.0];
mgg_hig_n2_bbh_cat11[2.0, 0.1, 10.0];
mggHig_bbh_cat11 = RooDoubleCB(mgg, mgg_hig_m0_bbh_cat11, mgg_hig_sigma_bbh_cat11, mgg_hig_alpha1_bbh_cat11, mgg_hig_n1_bbh_cat11, mgg_hig_alpha2_bbh_cat11, mgg_hig_n2_bbh_cat11);


Mjj_sig_m0_cat11[110.0, 99, 140];
Mjj_sig_sigma_cat11[25.0, 1.0, 60.0];
Mjj_sig_alpha1_cat11[1.0, 0.05, 10.0];
Mjj_sig_n1_cat11[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat11[1.0, 0.05, 10.0];
Mjj_sig_n2_cat11[2.0, 0.1, 10.0];
MjjSig_cat11 = RooDoubleCB(Mjj, Mjj_sig_m0_cat11, Mjj_sig_sigma_cat11, Mjj_sig_alpha1_cat11, Mjj_sig_n1_cat11, Mjj_sig_alpha2_cat11, Mjj_sig_n2_cat11);

Mjj_hig_par1_ggh_cat11[0.1, 0, 10];
Mjj_hig_par2_ggh_cat11[0.1, 0, 10];
Mjj_hig_par3_ggh_cat11[0.1, 0, 10];

Mjj_hig_par1_qqh_cat11[0.1, 0, 10];
Mjj_hig_par2_qqh_cat11[0.1, 0, 10];
Mjj_hig_par3_qqh_cat11[0.1, 0, 10];

Mjj_hig_m0_tth_cat11[130, 70, 190];
Mjj_hig_sigma_tth_cat11[50, 10, 100];
Mjj_hig_alpha1_tth_cat11[1.0, 0.01, 10];
Mjj_hig_n1_tth_cat11[1, 0.01, 10];
Mjj_hig_alpha2_tth_cat11[1.0, 0.01, 10];
Mjj_hig_n2_tth_cat11[1, 0.01, 10];
MjjHig_tth_cat11 = RooDoubleCB(Mjj, Mjj_hig_m0_tth_cat11, Mjj_hig_sigma_tth_cat11, Mjj_hig_alpha1_tth_cat11, Mjj_hig_n1_tth_cat11, Mjj_hig_alpha2_tth_cat11, Mjj_hig_n2_tth_cat11);

Mjj_hig_m0_vh_cat11[90, 70, 190];
Mjj_hig_sigma_vh_cat11[50, 10, 100];
Mjj_hig_alpha1_vh_cat11[1.0, 0.01, 10];
Mjj_hig_n1_vh_cat11[1, 0.01, 10];
Mjj_hig_alpha2_vh_cat11[1.0, 0.01, 10];
Mjj_hig_n2_vh_cat11[1, 0.01, 10];
MjjHig_vh_cat11 = RooDoubleCB(Mjj, Mjj_hig_m0_vh_cat11, Mjj_hig_sigma_vh_cat11, Mjj_hig_alpha1_vh_cat11, Mjj_hig_n1_vh_cat11, Mjj_hig_alpha2_vh_cat11, Mjj_hig_n2_vh_cat11);

Mjj_hig_m0_bbh_cat11[100, 10, 180];
Mjj_hig_sigma_bbh_cat11[50, 1.0, 100];
Mjj_hig_alpha1_bbh_cat11[1.0, 0.01, 10];
Mjj_hig_n1_bbh_cat11[1, 0.01, 10];
Mjj_hig_alpha2_bbh_cat11[1.0, 0.01, 10];
Mjj_hig_n2_bbh_cat11[1, 0.01, 10];
MjjHig_bbh_cat11 = RooDoubleCB(Mjj, Mjj_hig_m0_bbh_cat11, Mjj_hig_sigma_bbh_cat11, Mjj_hig_alpha1_bbh_cat11, Mjj_hig_n1_bbh_cat11, Mjj_hig_alpha2_bbh_cat11, Mjj_hig_n2_bbh_cat11);
mgg_sig_m0_cat2[125., 122, 127];
mgg_sig_sigma_cat2[1.0, 0.1, 3.0];
mgg_sig_alpha1_cat2[1.0, 0.05, 10.0];
mgg_sig_n1_cat2[2.0, 0.1, 10.0];
mgg_sig_alpha2_cat2[1.0, 0.05, 10.0];
mgg_sig_n2_cat2[2.0, 0.1, 10.0];
mggSig_cat2 = RooDoubleCB(mgg, mgg_sig_m0_cat2, mgg_sig_sigma_cat2, mgg_sig_alpha1_cat2, mgg_sig_n1_cat2, mgg_sig_alpha2_cat2, mgg_sig_n2_cat2);

mgg_hig_m0_ggh_cat2[124.2, 123, 125];
mgg_hig_sigma_ggh_cat2[2.0, 0.1, 3.0];
mgg_hig_alpha1_ggh_cat2[1.0, 0.05, 10.0];
mgg_hig_n1_ggh_cat2[2.0, 0.1, 10.0];
mgg_hig_alpha2_ggh_cat2[1.0, 0.05, 10.0];
mgg_hig_n2_ggh_cat2[2.0, 0.1, 10.0];
mggHig_ggh_cat2 = RooDoubleCB(mgg, mgg_hig_m0_ggh_cat2, mgg_hig_sigma_ggh_cat2, mgg_hig_alpha1_ggh_cat2, mgg_hig_n1_ggh_cat2, mgg_hig_alpha2_ggh_cat2, mgg_hig_n2_ggh_cat2);

mgg_hig_m0_tth_cat2[124.2, 123, 125];
mgg_hig_sigma_tth_cat2[2.0, 0.1, 3.0];
mgg_hig_alpha1_tth_cat2[1.0, 0.05, 10.0];
mgg_hig_n1_tth_cat2[2.0, 0.1, 10.0];
mgg_hig_alpha2_tth_cat2[1.0, 0.05, 10.0];
mgg_hig_n2_tth_cat2[2.0, 0.1, 10.0];
mggHig_tth_cat2 = RooDoubleCB(mgg, mgg_hig_m0_tth_cat2, mgg_hig_sigma_tth_cat2, mgg_hig_alpha1_tth_cat2, mgg_hig_n1_tth_cat2, mgg_hig_alpha2_tth_cat2, mgg_hig_n2_tth_cat2);

mgg_hig_m0_vh_cat2[124.2, 123, 125];
mgg_hig_sigma_vh_cat2[2.0, 0.1, 3.0];
mgg_hig_alpha1_vh_cat2[1.0, 0.05, 10.0];
mgg_hig_n1_vh_cat2[2.0, 0.1, 10.0];
mgg_hig_alpha2_vh_cat2[1.0, 0.05, 10.0];
mgg_hig_n2_vh_cat2[2.0, 0.1, 10.0];
mggHig_vh_cat2 = RooDoubleCB(mgg, mgg_hig_m0_vh_cat2, mgg_hig_sigma_vh_cat2, mgg_hig_alpha1_vh_cat2, mgg_hig_n1_vh_cat2, mgg_hig_alpha2_vh_cat2, mgg_hig_n2_vh_cat2);

mgg_hig_m0_qqh_cat2[124.2, 123, 125];
mgg_hig_sigma_qqh_cat2[2.0, 0.1, 3.0];
mgg_hig_alpha1_qqh_cat2[1.0, 0.05, 10.0];
mgg_hig_n1_qqh_cat2[2.0, 0.1, 10.0];
mgg_hig_alpha2_qqh_cat2[1.0, 0.05, 10.0];
mgg_hig_n2_qqh_cat2[2.0, 0.1, 10.0];
mggHig_qqh_cat2 = RooDoubleCB(mgg, mgg_hig_m0_qqh_cat2, mgg_hig_sigma_qqh_cat2, mgg_hig_alpha1_qqh_cat2, mgg_hig_n1_qqh_cat2, mgg_hig_alpha2_qqh_cat2, mgg_hig_n2_qqh_cat2);

mgg_hig_m0_bbh_cat2[124.2, 123, 125];
mgg_hig_sigma_bbh_cat2[2.0, 0.1, 3.0];
mgg_hig_alpha1_bbh_cat2[1.0, 0.05, 10.0];
mgg_hig_n1_bbh_cat2[2.0, 0.1, 10.0];
mgg_hig_alpha2_bbh_cat2[1.0, 0.05, 10.0];
mgg_hig_n2_bbh_cat2[2.0, 0.1, 10.0];
mggHig_bbh_cat2 = RooDoubleCB(mgg, mgg_hig_m0_bbh_cat2, mgg_hig_sigma_bbh_cat2, mgg_hig_alpha1_bbh_cat2, mgg_hig_n1_bbh_cat2, mgg_hig_alpha2_bbh_cat2, mgg_hig_n2_bbh_cat2);

Mjj_sig_m0_cat2[110.0, 99, 140];
Mjj_sig_sigma_cat2[10.0, 1.0, 60.0];
Mjj_sig_alpha1_cat2[1.0, 0.05, 10.0];
Mjj_sig_n1_cat2[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat2[1.0, 0.05, 10.0];
Mjj_sig_n2_cat2[2.0, 0.1, 5.0];
MjjSig_cat2 = RooDoubleCB(Mjj, Mjj_sig_m0_cat2, Mjj_sig_sigma_cat2, Mjj_sig_alpha1_cat2, Mjj_sig_n1_cat2, Mjj_sig_alpha2_cat2, Mjj_sig_n2_cat2);

Mjj_hig_par1_ggh_cat2[0.1, 0, 10];
Mjj_hig_par2_ggh_cat2[0.1, 0, 10];
Mjj_hig_par3_ggh_cat2[0.1, 0, 10];

Mjj_hig_par1_qqh_cat2[0.1, 0, 10];
Mjj_hig_par2_qqh_cat2[0.1, 0, 10];
Mjj_hig_par3_qqh_cat2[0.1, 0, 10];

Mjj_hig_m0_tth_cat2[130, 70, 190];
Mjj_hig_sigma_tth_cat2[50, 10, 100];
Mjj_hig_alpha1_tth_cat2[1.0, 0.01, 10];
Mjj_hig_n1_tth_cat2[1, 0.01, 10];
Mjj_hig_alpha2_tth_cat2[1.0, 0.01, 10];
Mjj_hig_n2_tth_cat2[1, 0.01, 10];
MjjHig_tth_cat2 = RooDoubleCB(Mjj, Mjj_hig_m0_tth_cat2, Mjj_hig_sigma_tth_cat2, Mjj_hig_alpha1_tth_cat2, Mjj_hig_n1_tth_cat2, Mjj_hig_alpha2_tth_cat2, Mjj_hig_n2_tth_cat2);

Mjj_hig_m0_vh_cat2[90, 70, 190];
Mjj_hig_sigma_vh_cat2[50, 10, 100];
Mjj_hig_alpha1_vh_cat2[1.0, 0.01, 10];
Mjj_hig_n1_vh_cat2[1, 0.01, 10];
Mjj_hig_alpha2_vh_cat2[1.0, 0.01, 10];
Mjj_hig_n2_vh_cat2[1, 0.01, 10];
MjjHig_vh_cat2 = RooDoubleCB(Mjj, Mjj_hig_m0_vh_cat2, Mjj_hig_sigma_vh_cat2, Mjj_hig_alpha1_vh_cat2, Mjj_hig_n1_vh_cat2, Mjj_hig_alpha2_vh_cat2, Mjj_hig_n2_vh_cat2);

Mjj_hig_m0_bbh_cat2[100, 10, 180];
Mjj_hig_sigma_bbh_cat2[50, 1.0, 100];
Mjj_hig_alpha1_bbh_cat2[1.0, 0.01, 10];
Mjj_hig_n1_bbh_cat2[1, 0.01, 10];
Mjj_hig_alpha2_bbh_cat2[1.0, 0.01, 10];
Mjj_hig_n2_bbh_cat2[1, 0.01, 10];
MjjHig_bbh_cat2 = RooDoubleCB(Mjj, Mjj_hig_m0_bbh_cat2, Mjj_hig_sigma_bbh_cat2, Mjj_hig_alpha1_bbh_cat2, Mjj_hig_n1_bbh_cat2, Mjj_hig_alpha2_bbh_cat2, Mjj_hig_n2_bbh_cat2);
mgg_sig_m0_cat3[125., 122, 127];
mgg_sig_sigma_cat3[1.0, 0.1, 3.0];
mgg_sig_alpha1_cat3[1.0, 0.05, 10.0];
mgg_sig_n1_cat3[2.0, 0.1, 10.0];
mgg_sig_alpha2_cat3[1.0, 0.05, 10.0];
mgg_sig_n2_cat3[2.0, 0.1, 10.0];
mggSig_cat3 = RooDoubleCB(mgg, mgg_sig_m0_cat3, mgg_sig_sigma_cat3, mgg_sig_alpha1_cat3, mgg_sig_n1_cat3, mgg_sig_alpha2_cat3, mgg_sig_n2_cat3);

mgg_hig_m0_ggh_cat3[124.2, 123, 125];
mgg_hig_sigma_ggh_cat3[2.0, 0.1, 3.0];
mgg_hig_alpha1_ggh_cat3[1.0, 0.05, 10.0];
mgg_hig_n1_ggh_cat3[2.0, 0.1, 10.0];
mgg_hig_alpha2_ggh_cat3[1.0, 0.05, 10.0];
mgg_hig_n2_ggh_cat3[2.0, 0.1, 10.0];
mggHig_ggh_cat3 = RooDoubleCB(mgg, mgg_hig_m0_ggh_cat3, mgg_hig_sigma_ggh_cat3, mgg_hig_alpha1_ggh_cat3, mgg_hig_n1_ggh_cat3, mgg_hig_alpha2_ggh_cat3, mgg_hig_n2_ggh_cat3);

mgg_hig_m0_tth_cat3[124.2, 123, 125];
mgg_hig_sigma_tth_cat3[2.0, 0.1, 3.0];
mgg_hig_alpha1_tth_cat3[1.0, 0.05, 10.0];
mgg_hig_n1_tth_cat3[2.0, 0.1, 10.0];
mgg_hig_alpha2_tth_cat3[1.0, 0.05, 10.0];
mgg_hig_n2_tth_cat3[2.0, 0.1, 10.0];
mggHig_tth_cat3 = RooDoubleCB(mgg, mgg_hig_m0_tth_cat3, mgg_hig_sigma_tth_cat3, mgg_hig_alpha1_tth_cat3, mgg_hig_n1_tth_cat3, mgg_hig_alpha2_tth_cat3, mgg_hig_n2_tth_cat3);

mgg_hig_m0_vh_cat3[124.2, 123, 125];
mgg_hig_sigma_vh_cat3[2.0, 0.1, 3.0];
mgg_hig_alpha1_vh_cat3[1.0, 0.05, 10.0];
mgg_hig_n1_vh_cat3[2.0, 0.1, 10.0];
mgg_hig_alpha2_vh_cat3[1.0, 0.05, 10.0];
mgg_hig_n2_vh_cat3[2.0, 0.1, 10.0];
mggHig_vh_cat3 = RooDoubleCB(mgg, mgg_hig_m0_vh_cat3, mgg_hig_sigma_vh_cat3, mgg_hig_alpha1_vh_cat3, mgg_hig_n1_vh_cat3, mgg_hig_alpha2_vh_cat3, mgg_hig_n2_vh_cat3);

mgg_hig_m0_qqh_cat3[124.2, 123, 125];
mgg_hig_sigma_qqh_cat3[2.0, 0.1, 3.0];
mgg_hig_alpha1_qqh_cat3[1.0, 0.05, 10.0];
mgg_hig_n1_qqh_cat3[2.0, 0.1, 10.0];
mgg_hig_alpha2_qqh_cat3[1.0, 0.05, 10.0];
mgg_hig_n2_qqh_cat3[2.0, 0.1, 10.0];
mggHig_qqh_cat3 = RooDoubleCB(mgg, mgg_hig_m0_qqh_cat3, mgg_hig_sigma_qqh_cat3, mgg_hig_alpha1_qqh_cat3, mgg_hig_n1_qqh_cat3, mgg_hig_alpha2_qqh_cat3, mgg_hig_n2_qqh_cat3);

mgg_hig_m0_bbh_cat3[124.2, 123, 125];
mgg_hig_sigma_bbh_cat3[2.0, 0.1, 3.0];
mgg_hig_alpha1_bbh_cat3[1.0, 0.05, 10.0];
mgg_hig_n1_bbh_cat3[2.0, 0.1, 10.0];
mgg_hig_alpha2_bbh_cat3[1.0, 0.05, 10.0];
mgg_hig_n2_bbh_cat3[2.0, 0.1, 10.0];
mggHig_bbh_cat3 = RooDoubleCB(mgg, mgg_hig_m0_bbh_cat3, mgg_hig_sigma_bbh_cat3, mgg_hig_alpha1_bbh_cat3, mgg_hig_n1_bbh_cat3, mgg_hig_alpha2_bbh_cat3, mgg_hig_n2_bbh_cat3);

Mjj_sig_m0_cat3[110.0, 99, 140];
Mjj_sig_sigma_cat3[10.0, 1.0, 60.0];
Mjj_sig_alpha1_cat3[1.0, 0.05, 10.0];
Mjj_sig_n1_cat3[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat3[1.0, 0.05, 10.0];
Mjj_sig_n2_cat3[2.0, 0.1, 5.0];
MjjSig_cat3 = RooDoubleCB(Mjj, Mjj_sig_m0_cat3, Mjj_sig_sigma_cat3, Mjj_sig_alpha1_cat3, Mjj_sig_n1_cat3, Mjj_sig_alpha2_cat3, Mjj_sig_n2_cat3);

Mjj_hig_par1_ggh_cat3[0.1, 0, 10];
Mjj_hig_par2_ggh_cat3[0.1, 0, 10];
Mjj_hig_par3_ggh_cat3[0.1, 0, 10];

Mjj_hig_par1_qqh_cat3[0.1, 0, 10];
Mjj_hig_par2_qqh_cat3[0.1, 0, 10];
Mjj_hig_par3_qqh_cat3[0.1, 0, 10];

Mjj_hig_m0_tth_cat3[130, 70, 190];
Mjj_hig_sigma_tth_cat3[50, 10, 100];
Mjj_hig_alpha1_tth_cat3[1.0, 0.01, 10];
Mjj_hig_n1_tth_cat3[1, 0.01, 10];
Mjj_hig_alpha2_tth_cat3[1.0, 0.01, 10];
Mjj_hig_n2_tth_cat3[1, 0.01, 10];
MjjHig_tth_cat3 = RooDoubleCB(Mjj, Mjj_hig_m0_tth_cat3, Mjj_hig_sigma_tth_cat3, Mjj_hig_alpha1_tth_cat3, Mjj_hig_n1_tth_cat3, Mjj_hig_alpha2_tth_cat3, Mjj_hig_n2_tth_cat3);

Mjj_hig_m0_vh_cat3[90, 70, 190];
Mjj_hig_sigma_vh_cat3[50, 10, 100];
Mjj_hig_alpha1_vh_cat3[1.0, 0.01, 10];
Mjj_hig_n1_vh_cat3[1, 0.01, 10];
Mjj_hig_alpha2_vh_cat3[1.0, 0.01, 10];
Mjj_hig_n2_vh_cat3[1, 0.01, 10];
MjjHig_vh_cat3 = RooDoubleCB(Mjj, Mjj_hig_m0_vh_cat3, Mjj_hig_sigma_vh_cat3, Mjj_hig_alpha1_vh_cat3, Mjj_hig_n1_vh_cat3, Mjj_hig_alpha2_vh_cat3, Mjj_hig_n2_vh_cat3);

Mjj_hig_m0_bbh_cat3[100, 10, 180];
Mjj_hig_sigma_bbh_cat3[50, 1.0, 100];
Mjj_hig_alpha1_bbh_cat3[1.0, 0.01, 10];
Mjj_hig_n1_bbh_cat3[1, 0.01, 10];
Mjj_hig_alpha2_bbh_cat3[1.0, 0.01, 10];
Mjj_hig_n2_bbh_cat3[1, 0.01, 10];
MjjHig_bbh_cat3 = RooDoubleCB(Mjj, Mjj_hig_m0_bbh_cat3, Mjj_hig_sigma_bbh_cat3, Mjj_hig_alpha1_bbh_cat3, Mjj_hig_n1_bbh_cat3, Mjj_hig_alpha2_bbh_cat3, Mjj_hig_n2_bbh_cat3);
mgg_sig_m0_cat4[125., 122, 127];
mgg_sig_sigma_cat4[1.0, 0.1, 3.0];
mgg_sig_alpha1_cat4[1.0, 0.05, 10.0];
mgg_sig_n1_cat4[2.0, 0.1, 10.0];
mgg_sig_alpha2_cat4[1.0, 0.05, 10.0];
mgg_sig_n2_cat4[2.0, 0.1, 10.0];
mggSig_cat4 = RooDoubleCB(mgg, mgg_sig_m0_cat4, mgg_sig_sigma_cat4, mgg_sig_alpha1_cat4, mgg_sig_n1_cat4, mgg_sig_alpha2_cat4, mgg_sig_n2_cat4);

mgg_hig_m0_ggh_cat4[124.2, 123, 125];
mgg_hig_sigma_ggh_cat4[2.0, 0.1, 3.0];
mgg_hig_alpha1_ggh_cat4[1.0, 0.05, 10.0];
mgg_hig_n1_ggh_cat4[2.0, 0.1, 10.0];
mgg_hig_alpha2_ggh_cat4[1.0, 0.05, 10.0];
mgg_hig_n2_ggh_cat4[2.0, 0.1, 10.0];
mggHig_ggh_cat4 = RooDoubleCB(mgg, mgg_hig_m0_ggh_cat4, mgg_hig_sigma_ggh_cat4, mgg_hig_alpha1_ggh_cat4, mgg_hig_n1_ggh_cat4, mgg_hig_alpha2_ggh_cat4, mgg_hig_n2_ggh_cat4);

mgg_hig_m0_tth_cat4[124.2, 123, 125];
mgg_hig_sigma_tth_cat4[2.0, 0.1, 3.0];
mgg_hig_alpha1_tth_cat4[1.0, 0.05, 10.0];
mgg_hig_n1_tth_cat4[2.0, 0.1, 10.0];
mgg_hig_alpha2_tth_cat4[1.0, 0.05, 10.0];
mgg_hig_n2_tth_cat4[2.0, 0.1, 10.0];
mggHig_tth_cat4 = RooDoubleCB(mgg, mgg_hig_m0_tth_cat4, mgg_hig_sigma_tth_cat4, mgg_hig_alpha1_tth_cat4, mgg_hig_n1_tth_cat4, mgg_hig_alpha2_tth_cat4, mgg_hig_n2_tth_cat4);

mgg_hig_m0_vh_cat4[124.2, 123, 125];
mgg_hig_sigma_vh_cat4[2.0, 0.1, 3.0];
mgg_hig_alpha1_vh_cat4[1.0, 0.05, 10.0];
mgg_hig_n1_vh_cat4[2.0, 0.1, 10.0];
mgg_hig_alpha2_vh_cat4[1.0, 0.05, 10.0];
mgg_hig_n2_vh_cat4[2.0, 0.1, 10.0];
mggHig_vh_cat4 = RooDoubleCB(mgg, mgg_hig_m0_vh_cat4, mgg_hig_sigma_vh_cat4, mgg_hig_alpha1_vh_cat4, mgg_hig_n1_vh_cat4, mgg_hig_alpha2_vh_cat4, mgg_hig_n2_vh_cat4);

mgg_hig_m0_qqh_cat4[124.2, 123, 125];
mgg_hig_sigma_qqh_cat4[2.0, 0.1, 3.0];
mgg_hig_alpha1_qqh_cat4[1.0, 0.05, 10.0];
mgg_hig_n1_qqh_cat4[2.0, 0.1, 10.0];
mgg_hig_alpha2_qqh_cat4[1.0, 0.05, 10.0];
mgg_hig_n2_qqh_cat4[2.0, 0.1, 10.0];
mggHig_qqh_cat4 = RooDoubleCB(mgg, mgg_hig_m0_qqh_cat4, mgg_hig_sigma_qqh_cat4, mgg_hig_alpha1_qqh_cat4, mgg_hig_n1_qqh_cat4, mgg_hig_alpha2_qqh_cat4, mgg_hig_n2_qqh_cat4);

mgg_hig_m0_bbh_cat4[124.2, 123, 125];
mgg_hig_sigma_bbh_cat4[2.0, 0.1, 3.0];
mgg_hig_alpha1_bbh_cat4[1.0, 0.05, 10.0];
mgg_hig_n1_bbh_cat4[2.0, 0.1, 10.0];
mgg_hig_alpha2_bbh_cat4[1.0, 0.05, 10.0];
mgg_hig_n2_bbh_cat4[2.0, 0.1, 10.0];
mggHig_bbh_cat4 = RooDoubleCB(mgg, mgg_hig_m0_bbh_cat4, mgg_hig_sigma_bbh_cat4, mgg_hig_alpha1_bbh_cat4, mgg_hig_n1_bbh_cat4, mgg_hig_alpha2_bbh_cat4, mgg_hig_n2_bbh_cat4);


Mjj_sig_m0_cat4[110.0, 99, 140];
Mjj_sig_sigma_cat4[10.0, 1.0, 60.0];
Mjj_sig_alpha1_cat4[1.0, 0.05, 10.0];
Mjj_sig_n1_cat4[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat4[1.0, 0.05, 10.0];
Mjj_sig_n2_cat4[2.0, 0.1, 10.0];
MjjSig_cat4 = RooDoubleCB(Mjj, Mjj_sig_m0_cat4, Mjj_sig_sigma_cat4, Mjj_sig_alpha1_cat4, Mjj_sig_n1_cat4, Mjj_sig_alpha2_cat4, Mjj_sig_n2_cat4);

Mjj_hig_par1_ggh_cat4[0.1, 0, 10];
Mjj_hig_par2_ggh_cat4[0.1, 0, 10];
Mjj_hig_par3_ggh_cat4[0.1, 0, 10];

Mjj_hig_par1_qqh_cat4[0.1, 0, 10];
Mjj_hig_par2_qqh_cat4[0.1, 0, 10];
Mjj_hig_par3_qqh_cat4[0.1, 0, 10];

Mjj_hig_m0_tth_cat4[130, 70, 190];
Mjj_hig_sigma_tth_cat4[50, 10, 100];
Mjj_hig_alpha1_tth_cat4[1.0, 0.01, 10];
Mjj_hig_n1_tth_cat4[1, 0.01, 10];
Mjj_hig_alpha2_tth_cat4[1.0, 0.01, 10];
Mjj_hig_n2_tth_cat4[1, 0.01, 10];
MjjHig_tth_cat4 = RooDoubleCB(Mjj, Mjj_hig_m0_tth_cat4, Mjj_hig_sigma_tth_cat4, Mjj_hig_alpha1_tth_cat4, Mjj_hig_n1_tth_cat4, Mjj_hig_alpha2_tth_cat4, Mjj_hig_n2_tth_cat4);

Mjj_hig_m0_vh_cat4[90, 70, 190];
Mjj_hig_sigma_vh_cat4[50, 10, 100];
Mjj_hig_alpha1_vh_cat4[1.0, 0.01, 10];
Mjj_hig_n1_vh_cat4[1, 0.01, 10];
Mjj_hig_alpha2_vh_cat4[1.0, 0.01, 10];
Mjj_hig_n2_vh_cat4[1, 0.01, 10];
MjjHig_vh_cat4 = RooDoubleCB(Mjj, Mjj_hig_m0_vh_cat4, Mjj_hig_sigma_vh_cat4, Mjj_hig_alpha1_vh_cat4, Mjj_hig_n1_vh_cat4, Mjj_hig_alpha2_vh_cat4, Mjj_hig_n2_vh_cat4);

Mjj_hig_m0_bbh_cat4[100, 10, 180];
Mjj_hig_sigma_bbh_cat4[50, 1.0, 100];
Mjj_hig_alpha1_bbh_cat4[1.0, 0.01, 10];
Mjj_hig_n1_bbh_cat4[1, 0.01, 10];
Mjj_hig_alpha2_bbh_cat4[1.0, 0.01, 10];
Mjj_hig_n2_bbh_cat4[1, 0.01, 10];
MjjHig_bbh_cat4 = RooDoubleCB(Mjj, Mjj_hig_m0_bbh_cat4, Mjj_hig_sigma_bbh_cat4, Mjj_hig_alpha1_bbh_cat4, Mjj_hig_n1_bbh_cat4, Mjj_hig_alpha2_bbh_cat4, Mjj_hig_n2_bbh_cat4);
mgg_sig_m0_cat5[125., 122, 127];
mgg_sig_sigma_cat5[1.0, 0.1, 3.0];
mgg_sig_alpha1_cat5[1.0, 0.05, 10.0];
mgg_sig_n1_cat5[2.0, 0.1, 10.0];
mgg_sig_alpha2_cat5[1.0, 0.05, 10.0];
mgg_sig_n2_cat5[2.0, 0.1, 10.0];
mggSig_cat5 = RooDoubleCB(mgg, mgg_sig_m0_cat5, mgg_sig_sigma_cat5, mgg_sig_alpha1_cat5, mgg_sig_n1_cat5, mgg_sig_alpha2_cat5, mgg_sig_n2_cat5);

mgg_hig_m0_ggh_cat5[124.2, 123, 125];
mgg_hig_sigma_ggh_cat5[2.0, 0.1, 3.0];
mgg_hig_alpha1_ggh_cat5[1.0, 0.05, 10.0];
mgg_hig_n1_ggh_cat5[2.0, 0.1, 10.0];
mgg_hig_alpha2_ggh_cat5[1.0, 0.05, 10.0];
mgg_hig_n2_ggh_cat5[2.0, 0.1, 10.0];
mggHig_ggh_cat5 = RooDoubleCB(mgg, mgg_hig_m0_ggh_cat5, mgg_hig_sigma_ggh_cat5, mgg_hig_alpha1_ggh_cat5, mgg_hig_n1_ggh_cat5, mgg_hig_alpha2_ggh_cat5, mgg_hig_n2_ggh_cat5);

mgg_hig_m0_tth_cat5[124.2, 123, 125];
mgg_hig_sigma_tth_cat5[2.0, 0.1, 3.0];
mgg_hig_alpha1_tth_cat5[1.0, 0.05, 10.0];
mgg_hig_n1_tth_cat5[2.0, 0.1, 10.0];
mgg_hig_alpha2_tth_cat5[1.0, 0.05, 10.0];
mgg_hig_n2_tth_cat5[2.0, 0.1, 10.0];
mggHig_tth_cat5 = RooDoubleCB(mgg, mgg_hig_m0_tth_cat5, mgg_hig_sigma_tth_cat5, mgg_hig_alpha1_tth_cat5, mgg_hig_n1_tth_cat5, mgg_hig_alpha2_tth_cat5, mgg_hig_n2_tth_cat5);

mgg_hig_m0_vh_cat5[124.2, 123, 125];
mgg_hig_sigma_vh_cat5[2.0, 0.1, 3.0];
mgg_hig_alpha1_vh_cat5[1.0, 0.05, 10.0];
mgg_hig_n1_vh_cat5[2.0, 0.1, 10.0];
mgg_hig_alpha2_vh_cat5[1.0, 0.05, 10.0];
mgg_hig_n2_vh_cat5[2.0, 0.1, 10.0];
mggHig_vh_cat5 = RooDoubleCB(mgg, mgg_hig_m0_vh_cat5, mgg_hig_sigma_vh_cat5, mgg_hig_alpha1_vh_cat5, mgg_hig_n1_vh_cat5, mgg_hig_alpha2_vh_cat5, mgg_hig_n2_vh_cat5);

mgg_hig_m0_qqh_cat5[124.2, 123, 125];
mgg_hig_sigma_qqh_cat5[2.0, 0.1, 3.0];
mgg_hig_alpha1_qqh_cat5[1.0, 0.05, 10.0];
mgg_hig_n1_qqh_cat5[2.0, 0.1, 10.0];
mgg_hig_alpha2_qqh_cat5[1.0, 0.05, 10.0];
mgg_hig_n2_qqh_cat5[2.0, 0.1, 10.0];
mggHig_qqh_cat5 = RooDoubleCB(mgg, mgg_hig_m0_qqh_cat5, mgg_hig_sigma_qqh_cat5, mgg_hig_alpha1_qqh_cat5, mgg_hig_n1_qqh_cat5, mgg_hig_alpha2_qqh_cat5, mgg_hig_n2_qqh_cat5);

mgg_hig_m0_bbh_cat5[124.2, 123, 125];
mgg_hig_sigma_bbh_cat5[2.0, 0.1, 3.0];
mgg_hig_alpha1_bbh_cat5[1.0, 0.05, 10.0];
mgg_hig_n1_bbh_cat5[2.0, 0.1, 10.0];
mgg_hig_alpha2_bbh_cat5[1.0, 0.05, 10.0];
mgg_hig_n2_bbh_cat5[2.0, 0.1, 10.0];
mggHig_bbh_cat5 = RooDoubleCB(mgg, mgg_hig_m0_bbh_cat5, mgg_hig_sigma_bbh_cat5, mgg_hig_alpha1_bbh_cat5, mgg_hig_n1_bbh_cat5, mgg_hig_alpha2_bbh_cat5, mgg_hig_n2_bbh_cat5);


Mjj_sig_m0_cat5[110.0, 99, 140];
Mjj_sig_sigma_cat5[10.0, 1.0, 60.0];
Mjj_sig_alpha1_cat5[1.0, 0.05, 10.0];
Mjj_sig_n1_cat5[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat5[1.0, 0.05, 10.0];
Mjj_sig_n2_cat5[2.0, 0.1, 10.0];
MjjSig_cat5 = RooDoubleCB(Mjj, Mjj_sig_m0_cat5, Mjj_sig_sigma_cat5, Mjj_sig_alpha1_cat5, Mjj_sig_n1_cat5, Mjj_sig_alpha2_cat5, Mjj_sig_n2_cat5);

Mjj_hig_par1_ggh_cat5[0.1, 0, 10];
Mjj_hig_par2_ggh_cat5[0.1, 0, 10];
Mjj_hig_par3_ggh_cat5[0.1, 0, 10];

Mjj_hig_par1_qqh_cat5[0.1, 0, 10];
Mjj_hig_par2_qqh_cat5[0.1, 0, 10];
Mjj_hig_par3_qqh_cat5[0.1, 0, 10];

Mjj_hig_m0_tth_cat5[130, 70, 190];
Mjj_hig_sigma_tth_cat5[50, 10, 100];
Mjj_hig_alpha1_tth_cat5[1.0, 0.01, 10];
Mjj_hig_n1_tth_cat5[1, 0.01, 10];
Mjj_hig_alpha2_tth_cat5[1.0, 0.01, 10];
Mjj_hig_n2_tth_cat5[1, 0.01, 10];
MjjHig_tth_cat5 = RooDoubleCB(Mjj, Mjj_hig_m0_tth_cat5, Mjj_hig_sigma_tth_cat5, Mjj_hig_alpha1_tth_cat5, Mjj_hig_n1_tth_cat5, Mjj_hig_alpha2_tth_cat5, Mjj_hig_n2_tth_cat5);

Mjj_hig_m0_vh_cat5[90, 70, 190];
Mjj_hig_sigma_vh_cat5[50, 10, 100];
Mjj_hig_alpha1_vh_cat5[1.0, 0.01, 10];
Mjj_hig_n1_vh_cat5[1, 0.01, 10];
Mjj_hig_alpha2_vh_cat5[1.0, 0.01, 10];
Mjj_hig_n2_vh_cat5[1, 0.01, 10];
MjjHig_vh_cat5 = RooDoubleCB(Mjj, Mjj_hig_m0_vh_cat5, Mjj_hig_sigma_vh_cat5, Mjj_hig_alpha1_vh_cat5, Mjj_hig_n1_vh_cat5, Mjj_hig_alpha2_vh_cat5, Mjj_hig_n2_vh_cat5);

Mjj_hig_m0_bbh_cat5[100, 10, 180];
Mjj_hig_sigma_bbh_cat5[50, 1.0, 100];
Mjj_hig_alpha1_bbh_cat5[1.0, 0.01, 10];
Mjj_hig_n1_bbh_cat5[1, 0.01, 10];
Mjj_hig_alpha2_bbh_cat5[1.0, 0.01, 10];
Mjj_hig_n2_bbh_cat5[1, 0.01, 10];
MjjHig_bbh_cat5 = RooDoubleCB(Mjj, Mjj_hig_m0_bbh_cat5, Mjj_hig_sigma_bbh_cat5, Mjj_hig_alpha1_bbh_cat5, Mjj_hig_n1_bbh_cat5, Mjj_hig_alpha2_bbh_cat5, Mjj_hig_n2_bbh_cat5);
mgg_sig_m0_cat6[125., 122, 127];
mgg_sig_sigma_cat6[1.0, 0.1, 3.0];
mgg_sig_alpha1_cat6[1.0, 0.05, 10.0];
mgg_sig_n1_cat6[2.0, 0.1, 10.0];
mgg_sig_alpha2_cat6[1.0, 0.05, 10.0];
mgg_sig_n2_cat6[2.0, 0.1, 10.0];
mggSig_cat6 = RooDoubleCB(mgg, mgg_sig_m0_cat6, mgg_sig_sigma_cat6, mgg_sig_alpha1_cat6, mgg_sig_n1_cat6, mgg_sig_alpha2_cat6, mgg_sig_n2_cat6);

mgg_hig_m0_ggh_cat6[124.2, 123, 125];
mgg_hig_sigma_ggh_cat6[2.0, 0.1, 3.0];
mgg_hig_alpha1_ggh_cat6[1.0, 0.05, 10.0];
mgg_hig_n1_ggh_cat6[2.0, 0.1, 10.0];
mgg_hig_alpha2_ggh_cat6[1.0, 0.05, 10.0];
mgg_hig_n2_ggh_cat6[2.0, 0.1, 10.0];
mggHig_ggh_cat6 = RooDoubleCB(mgg, mgg_hig_m0_ggh_cat6, mgg_hig_sigma_ggh_cat6, mgg_hig_alpha1_ggh_cat6, mgg_hig_n1_ggh_cat6, mgg_hig_alpha2_ggh_cat6, mgg_hig_n2_ggh_cat6);

mgg_hig_m0_tth_cat6[124.2, 123, 125];
mgg_hig_sigma_tth_cat6[2.0, 0.1, 3.0];
mgg_hig_alpha1_tth_cat6[1.0, 0.05, 10.0];
mgg_hig_n1_tth_cat6[2.0, 0.1, 10.0];
mgg_hig_alpha2_tth_cat6[1.0, 0.05, 10.0];
mgg_hig_n2_tth_cat6[2.0, 0.1, 10.0];
mggHig_tth_cat6 = RooDoubleCB(mgg, mgg_hig_m0_tth_cat6, mgg_hig_sigma_tth_cat6, mgg_hig_alpha1_tth_cat6, mgg_hig_n1_tth_cat6, mgg_hig_alpha2_tth_cat6, mgg_hig_n2_tth_cat6);

mgg_hig_m0_vh_cat6[124.2, 123, 125];
mgg_hig_sigma_vh_cat6[2.0, 0.1, 3.0];
mgg_hig_alpha1_vh_cat6[1.0, 0.05, 10.0];
mgg_hig_n1_vh_cat6[2.0, 0.1, 10.0];
mgg_hig_alpha2_vh_cat6[1.0, 0.05, 10.0];
mgg_hig_n2_vh_cat6[2.0, 0.1, 10.0];
mggHig_vh_cat6 = RooDoubleCB(mgg, mgg_hig_m0_vh_cat6, mgg_hig_sigma_vh_cat6, mgg_hig_alpha1_vh_cat6, mgg_hig_n1_vh_cat6, mgg_hig_alpha2_vh_cat6, mgg_hig_n2_vh_cat6);

mgg_hig_m0_qqh_cat6[124.2, 123, 125];
mgg_hig_sigma_qqh_cat6[2.0, 0.1, 3.0];
mgg_hig_alpha1_qqh_cat6[1.0, 0.05, 10.0];
mgg_hig_n1_qqh_cat6[2.0, 0.1, 10.0];
mgg_hig_alpha2_qqh_cat6[1.0, 0.05, 10.0];
mgg_hig_n2_qqh_cat6[2.0, 0.1, 10.0];
mggHig_qqh_cat6 = RooDoubleCB(mgg, mgg_hig_m0_qqh_cat6, mgg_hig_sigma_qqh_cat6, mgg_hig_alpha1_qqh_cat6, mgg_hig_n1_qqh_cat6, mgg_hig_alpha2_qqh_cat6, mgg_hig_n2_qqh_cat6);

mgg_hig_m0_bbh_cat6[124.2, 123, 125];
mgg_hig_sigma_bbh_cat6[2.0, 0.1, 3.0];
mgg_hig_alpha1_bbh_cat6[1.0, 0.05, 10.0];
mgg_hig_n1_bbh_cat6[2.0, 0.1, 10.0];
mgg_hig_alpha2_bbh_cat6[1.0, 0.05, 10.0];
mgg_hig_n2_bbh_cat6[2.0, 0.1, 10.0];
mggHig_bbh_cat6 = RooDoubleCB(mgg, mgg_hig_m0_bbh_cat6, mgg_hig_sigma_bbh_cat6, mgg_hig_alpha1_bbh_cat6, mgg_hig_n1_bbh_cat6, mgg_hig_alpha2_bbh_cat6, mgg_hig_n2_bbh_cat6);


Mjj_sig_m0_cat6[110.0, 99, 140];
Mjj_sig_sigma_cat6[10.0, 1.0, 60.0];
Mjj_sig_alpha1_cat6[1.0, 0.05, 10.0];
Mjj_sig_n1_cat6[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat6[1.0, 0.05, 10.0];
Mjj_sig_n2_cat6[2.0, 0.1, 10.0];
MjjSig_cat6 = RooDoubleCB(Mjj, Mjj_sig_m0_cat6, Mjj_sig_sigma_cat6, Mjj_sig_alpha1_cat6, Mjj_sig_n1_cat6, Mjj_sig_alpha2_cat6, Mjj_sig_n2_cat6);

Mjj_hig_par1_ggh_cat6[0.1, 0, 10];
Mjj_hig_par2_ggh_cat6[0.1, 0, 10];
Mjj_hig_par3_ggh_cat6[0.1, 0, 10];

Mjj_hig_par1_qqh_cat6[0.1, 0, 10];
Mjj_hig_par2_qqh_cat6[0.1, 0, 10];
Mjj_hig_par3_qqh_cat6[0.1, 0, 10];

Mjj_hig_m0_tth_cat6[130, 70, 190];
Mjj_hig_sigma_tth_cat6[50, 10, 100];
Mjj_hig_alpha1_tth_cat6[1.0, 0.01, 10];
Mjj_hig_n1_tth_cat6[1, 0.01, 10];
Mjj_hig_alpha2_tth_cat6[1.0, 0.01, 10];
Mjj_hig_n2_tth_cat6[1, 0.01, 10];
MjjHig_tth_cat6 = RooDoubleCB(Mjj, Mjj_hig_m0_tth_cat6, Mjj_hig_sigma_tth_cat6, Mjj_hig_alpha1_tth_cat6, Mjj_hig_n1_tth_cat6, Mjj_hig_alpha2_tth_cat6, Mjj_hig_n2_tth_cat6);

Mjj_hig_m0_vh_cat6[90, 70, 190];
Mjj_hig_sigma_vh_cat6[50, 10, 100];
Mjj_hig_alpha1_vh_cat6[1.0, 0.01, 10];
Mjj_hig_n1_vh_cat6[1, 0.01, 10];
Mjj_hig_alpha2_vh_cat6[1.0, 0.01, 10];
Mjj_hig_n2_vh_cat6[1, 0.01, 10];
MjjHig_vh_cat6 = RooDoubleCB(Mjj, Mjj_hig_m0_vh_cat6, Mjj_hig_sigma_vh_cat6, Mjj_hig_alpha1_vh_cat6, Mjj_hig_n1_vh_cat6, Mjj_hig_alpha2_vh_cat6, Mjj_hig_n2_vh_cat6);

Mjj_hig_m0_bbh_cat6[100, 10, 180];
Mjj_hig_sigma_bbh_cat6[50, 1.0, 100];
Mjj_hig_alpha1_bbh_cat6[1.0, 0.01, 10];
Mjj_hig_n1_bbh_cat6[1, 0.01, 10];
Mjj_hig_alpha2_bbh_cat6[1.0, 0.01, 10];
Mjj_hig_n2_bbh_cat6[1, 0.01, 10];
MjjHig_bbh_cat6 = RooDoubleCB(Mjj, Mjj_hig_m0_bbh_cat6, Mjj_hig_sigma_bbh_cat6, Mjj_hig_alpha1_bbh_cat6, Mjj_hig_n1_bbh_cat6, Mjj_hig_alpha2_bbh_cat6, Mjj_hig_n2_bbh_cat6);
mgg_sig_m0_cat7[125., 122, 127];
mgg_sig_sigma_cat7[1.0, 0.1, 3.0];
mgg_sig_alpha1_cat7[1.0, 0.05, 10.0];
mgg_sig_n1_cat7[2.0, 0.1, 10.0];
mgg_sig_alpha2_cat7[1.0, 0.05, 10.0];
mgg_sig_n2_cat7[2.0, 0.1, 10.0];
mggSig_cat7 = RooDoubleCB(mgg, mgg_sig_m0_cat7, mgg_sig_sigma_cat7, mgg_sig_alpha1_cat7, mgg_sig_n1_cat7, mgg_sig_alpha2_cat7, mgg_sig_n2_cat7);

mgg_hig_m0_ggh_cat7[124.2, 123, 125];
mgg_hig_sigma_ggh_cat7[2.0, 0.1, 3.0];
mgg_hig_alpha1_ggh_cat7[1.0, 0.05, 10.0];
mgg_hig_n1_ggh_cat7[2.0, 0.1, 10.0];
mgg_hig_alpha2_ggh_cat7[1.0, 0.05, 10.0];
mgg_hig_n2_ggh_cat7[2.0, 0.1, 10.0];
mggHig_ggh_cat7 = RooDoubleCB(mgg, mgg_hig_m0_ggh_cat7, mgg_hig_sigma_ggh_cat7, mgg_hig_alpha1_ggh_cat7, mgg_hig_n1_ggh_cat7, mgg_hig_alpha2_ggh_cat7, mgg_hig_n2_ggh_cat7);

mgg_hig_m0_tth_cat7[124.2, 123, 125];
mgg_hig_sigma_tth_cat7[2.0, 0.1, 3.0];
mgg_hig_alpha1_tth_cat7[1.0, 0.05, 10.0];
mgg_hig_n1_tth_cat7[2.0, 0.1, 10.0];
mgg_hig_alpha2_tth_cat7[1.0, 0.05, 10.0];
mgg_hig_n2_tth_cat7[2.0, 0.1, 10.0];
mggHig_tth_cat7 = RooDoubleCB(mgg, mgg_hig_m0_tth_cat7, mgg_hig_sigma_tth_cat7, mgg_hig_alpha1_tth_cat7, mgg_hig_n1_tth_cat7, mgg_hig_alpha2_tth_cat7, mgg_hig_n2_tth_cat7);

mgg_hig_m0_vh_cat7[124.2, 123, 125];
mgg_hig_sigma_vh_cat7[2.0, 0.1, 3.0];
mgg_hig_alpha1_vh_cat7[1.0, 0.05, 10.0];
mgg_hig_n1_vh_cat7[2.0, 0.1, 10.0];
mgg_hig_alpha2_vh_cat7[1.0, 0.05, 10.0];
mgg_hig_n2_vh_cat7[2.0, 0.1, 10.0];
mggHig_vh_cat7 = RooDoubleCB(mgg, mgg_hig_m0_vh_cat7, mgg_hig_sigma_vh_cat7, mgg_hig_alpha1_vh_cat7, mgg_hig_n1_vh_cat7, mgg_hig_alpha2_vh_cat7, mgg_hig_n2_vh_cat7);

mgg_hig_m0_qqh_cat7[124.2, 123, 125];
mgg_hig_sigma_qqh_cat7[2.0, 0.1, 3.0];
mgg_hig_alpha1_qqh_cat7[1.0, 0.05, 10.0];
mgg_hig_n1_qqh_cat7[2.0, 0.1, 10.0];
mgg_hig_alpha2_qqh_cat7[1.0, 0.05, 10.0];
mgg_hig_n2_qqh_cat7[2.0, 0.1, 10.0];
mggHig_qqh_cat7 = RooDoubleCB(mgg, mgg_hig_m0_qqh_cat7, mgg_hig_sigma_qqh_cat7, mgg_hig_alpha1_qqh_cat7, mgg_hig_n1_qqh_cat7, mgg_hig_alpha2_qqh_cat7, mgg_hig_n2_qqh_cat7);

mgg_hig_m0_bbh_cat7[124.2, 123, 125];
mgg_hig_sigma_bbh_cat7[2.0, 0.1, 3.0];
mgg_hig_alpha1_bbh_cat7[1.0, 0.05, 10.0];
mgg_hig_n1_bbh_cat7[2.0, 0.1, 10.0];
mgg_hig_alpha2_bbh_cat7[1.0, 0.05, 10.0];
mgg_hig_n2_bbh_cat7[2.0, 0.1, 10.0];
mggHig_bbh_cat7 = RooDoubleCB(mgg, mgg_hig_m0_bbh_cat7, mgg_hig_sigma_bbh_cat7, mgg_hig_alpha1_bbh_cat7, mgg_hig_n1_bbh_cat7, mgg_hig_alpha2_bbh_cat7, mgg_hig_n2_bbh_cat7);


Mjj_sig_m0_cat7[110.0, 99, 140];
Mjj_sig_sigma_cat7[10.0, 1.0, 60.0];
Mjj_sig_alpha1_cat7[1.0, 0.05, 10.0];
Mjj_sig_n1_cat7[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat7[1.0, 0.05, 10.0];
Mjj_sig_n2_cat7[2.0, 0.1, 10.0];
MjjSig_cat7 = RooDoubleCB(Mjj, Mjj_sig_m0_cat7, Mjj_sig_sigma_cat7, Mjj_sig_alpha1_cat7, Mjj_sig_n1_cat7, Mjj_sig_alpha2_cat7, Mjj_sig_n2_cat7);

Mjj_hig_par1_ggh_cat7[0.1, 0, 10];
Mjj_hig_par2_ggh_cat7[0.1, 0, 10];
Mjj_hig_par3_ggh_cat7[0.1, 0, 10];

Mjj_hig_par1_qqh_cat7[0.1, 0, 10];
Mjj_hig_par2_qqh_cat7[0.1, 0, 10];
Mjj_hig_par3_qqh_cat7[0.1, 0, 10];

Mjj_hig_m0_tth_cat7[130, 70, 190];
Mjj_hig_sigma_tth_cat7[50, 10, 100];
Mjj_hig_alpha1_tth_cat7[1.0, 0.01, 10];
Mjj_hig_n1_tth_cat7[1, 0.01, 10];
Mjj_hig_alpha2_tth_cat7[1.0, 0.01, 10];
Mjj_hig_n2_tth_cat7[1, 0.01, 10];
MjjHig_tth_cat7 = RooDoubleCB(Mjj, Mjj_hig_m0_tth_cat7, Mjj_hig_sigma_tth_cat7, Mjj_hig_alpha1_tth_cat7, Mjj_hig_n1_tth_cat7, Mjj_hig_alpha2_tth_cat7, Mjj_hig_n2_tth_cat7);

Mjj_hig_m0_vh_cat7[90, 70, 190];
Mjj_hig_sigma_vh_cat7[50, 10, 100];
Mjj_hig_alpha1_vh_cat7[1.0, 0.01, 10];
Mjj_hig_n1_vh_cat7[1, 0.01, 10];
Mjj_hig_alpha2_vh_cat7[1.0, 0.01, 10];
Mjj_hig_n2_vh_cat7[1, 0.01, 10];
MjjHig_vh_cat7 = RooDoubleCB(Mjj, Mjj_hig_m0_vh_cat7, Mjj_hig_sigma_vh_cat7, Mjj_hig_alpha1_vh_cat7, Mjj_hig_n1_vh_cat7, Mjj_hig_alpha2_vh_cat7, Mjj_hig_n2_vh_cat7);

Mjj_hig_m0_bbh_cat7[100, 10, 180];
Mjj_hig_sigma_bbh_cat7[50, 1.0, 100];
Mjj_hig_alpha1_bbh_cat7[1.0, 0.01, 10];
Mjj_hig_n1_bbh_cat7[1, 0.01, 10];
Mjj_hig_alpha2_bbh_cat7[1.0, 0.01, 10];
Mjj_hig_n2_bbh_cat7[1, 0.01, 10];
MjjHig_bbh_cat7 = RooDoubleCB(Mjj, Mjj_hig_m0_bbh_cat7, Mjj_hig_sigma_bbh_cat7, Mjj_hig_alpha1_bbh_cat7, Mjj_hig_n1_bbh_cat7, Mjj_hig_alpha2_bbh_cat7, Mjj_hig_n2_bbh_cat7);
mgg_sig_m0_cat8[125., 122, 127];
mgg_sig_sigma_cat8[1.0, 0.1, 3.0];
mgg_sig_alpha1_cat8[1.0, 0.05, 10.0];
mgg_sig_n1_cat8[2.0, 0.1, 10.0];
mgg_sig_alpha2_cat8[1.0, 0.05, 10.0];
mgg_sig_n2_cat8[2.0, 0.1, 10.0];
mggSig_cat8 = RooDoubleCB(mgg, mgg_sig_m0_cat8, mgg_sig_sigma_cat8, mgg_sig_alpha1_cat8, mgg_sig_n1_cat8, mgg_sig_alpha2_cat8, mgg_sig_n2_cat8);

mgg_hig_m0_ggh_cat8[124.2, 123, 125];
mgg_hig_sigma_ggh_cat8[2.0, 0.1, 3.0];
mgg_hig_alpha1_ggh_cat8[1.0, 0.05, 10.0];
mgg_hig_n1_ggh_cat8[2.0, 0.1, 10.0];
mgg_hig_alpha2_ggh_cat8[1.0, 0.05, 10.0];
mgg_hig_n2_ggh_cat8[2.0, 0.1, 10.0];
mggHig_ggh_cat8 = RooDoubleCB(mgg, mgg_hig_m0_ggh_cat8, mgg_hig_sigma_ggh_cat8, mgg_hig_alpha1_ggh_cat8, mgg_hig_n1_ggh_cat8, mgg_hig_alpha2_ggh_cat8, mgg_hig_n2_ggh_cat8);

mgg_hig_m0_tth_cat8[124.2, 123, 125];
mgg_hig_sigma_tth_cat8[2.0, 0.1, 3.0];
mgg_hig_alpha1_tth_cat8[1.0, 0.05, 10.0];
mgg_hig_n1_tth_cat8[2.0, 0.1, 10.0];
mgg_hig_alpha2_tth_cat8[1.0, 0.05, 10.0];
mgg_hig_n2_tth_cat8[2.0, 0.1, 10.0];
mggHig_tth_cat8 = RooDoubleCB(mgg, mgg_hig_m0_tth_cat8, mgg_hig_sigma_tth_cat8, mgg_hig_alpha1_tth_cat8, mgg_hig_n1_tth_cat8, mgg_hig_alpha2_tth_cat8, mgg_hig_n2_tth_cat8);

mgg_hig_m0_vh_cat8[124.2, 123, 125];
mgg_hig_sigma_vh_cat8[2.0, 0.1, 3.0];
mgg_hig_alpha1_vh_cat8[1.0, 0.05, 10.0];
mgg_hig_n1_vh_cat8[2.0, 0.1, 10.0];
mgg_hig_alpha2_vh_cat8[1.0, 0.05, 10.0];
mgg_hig_n2_vh_cat8[2.0, 0.1, 10.0];
mggHig_vh_cat8 = RooDoubleCB(mgg, mgg_hig_m0_vh_cat8, mgg_hig_sigma_vh_cat8, mgg_hig_alpha1_vh_cat8, mgg_hig_n1_vh_cat8, mgg_hig_alpha2_vh_cat8, mgg_hig_n2_vh_cat8);

mgg_hig_m0_qqh_cat8[124.2, 123, 125];
mgg_hig_sigma_qqh_cat8[2.0, 0.1, 3.0];
mgg_hig_alpha1_qqh_cat8[1.0, 0.05, 10.0];
mgg_hig_n1_qqh_cat8[2.0, 0.1, 10.0];
mgg_hig_alpha2_qqh_cat8[1.0, 0.05, 10.0];
mgg_hig_n2_qqh_cat8[2.0, 0.1, 10.0];
mggHig_qqh_cat8 = RooDoubleCB(mgg, mgg_hig_m0_qqh_cat8, mgg_hig_sigma_qqh_cat8, mgg_hig_alpha1_qqh_cat8, mgg_hig_n1_qqh_cat8, mgg_hig_alpha2_qqh_cat8, mgg_hig_n2_qqh_cat8);

mgg_hig_m0_bbh_cat8[124.2, 123, 125];
mgg_hig_sigma_bbh_cat8[2.0, 0.1, 3.0];
mgg_hig_alpha1_bbh_cat8[1.0, 0.05, 10.0];
mgg_hig_n1_bbh_cat8[2.0, 0.1, 10.0];
mgg_hig_alpha2_bbh_cat8[1.0, 0.05, 10.0];
mgg_hig_n2_bbh_cat8[2.0, 0.1, 10.0];
mggHig_bbh_cat8 = RooDoubleCB(mgg, mgg_hig_m0_bbh_cat8, mgg_hig_sigma_bbh_cat8, mgg_hig_alpha1_bbh_cat8, mgg_hig_n1_bbh_cat8, mgg_hig_alpha2_bbh_cat8, mgg_hig_n2_bbh_cat8);


Mjj_sig_m0_cat8[110.0, 99, 140];
Mjj_sig_sigma_cat8[20.0, 1.0, 60.0];
Mjj_sig_alpha1_cat8[1.0, 0.05, 10.0];
Mjj_sig_n1_cat8[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat8[1.0, 0.05, 10.0];
Mjj_sig_n2_cat8[2.0, 0.1, 10.0];
MjjSig_cat8 = RooDoubleCB(Mjj, Mjj_sig_m0_cat8, Mjj_sig_sigma_cat8, Mjj_sig_alpha1_cat8, Mjj_sig_n1_cat8, Mjj_sig_alpha2_cat8, Mjj_sig_n2_cat8);

Mjj_hig_par1_ggh_cat8[0.1, 0, 10];
Mjj_hig_par2_ggh_cat8[0.1, 0, 10];
Mjj_hig_par3_ggh_cat8[0.1, 0, 10];

Mjj_hig_par1_qqh_cat8[0.1, 0, 10];
Mjj_hig_par2_qqh_cat8[0.1, 0, 10];
Mjj_hig_par3_qqh_cat8[0.1, 0, 10];

Mjj_hig_m0_tth_cat8[130, 70, 190];
Mjj_hig_sigma_tth_cat8[50, 10, 100];
Mjj_hig_alpha1_tth_cat8[1.0, 0.01, 10];
Mjj_hig_n1_tth_cat8[1, 0.01, 10];
Mjj_hig_alpha2_tth_cat8[1.0, 0.01, 10];
Mjj_hig_n2_tth_cat8[1, 0.01, 10];
MjjHig_tth_cat8 = RooDoubleCB(Mjj, Mjj_hig_m0_tth_cat8, Mjj_hig_sigma_tth_cat8, Mjj_hig_alpha1_tth_cat8, Mjj_hig_n1_tth_cat8, Mjj_hig_alpha2_tth_cat8, Mjj_hig_n2_tth_cat8);

Mjj_hig_m0_vh_cat8[90, 70, 190];
Mjj_hig_sigma_vh_cat8[50, 10, 100];
Mjj_hig_alpha1_vh_cat8[1.0, 0.01, 10];
Mjj_hig_n1_vh_cat8[1, 0.01, 10];
Mjj_hig_alpha2_vh_cat8[1.0, 0.01, 10];
Mjj_hig_n2_vh_cat8[1, 0.01, 10];
MjjHig_vh_cat8 = RooDoubleCB(Mjj, Mjj_hig_m0_vh_cat8, Mjj_hig_sigma_vh_cat8, Mjj_hig_alpha1_vh_cat8, Mjj_hig_n1_vh_cat8, Mjj_hig_alpha2_vh_cat8, Mjj_hig_n2_vh_cat8);

Mjj_hig_m0_bbh_cat8[100, 10, 180];
Mjj_hig_sigma_bbh_cat8[50, 1.0, 100];
Mjj_hig_alpha1_bbh_cat8[1.0, 0.01, 10];
Mjj_hig_n1_bbh_cat8[1, 0.01, 10];
Mjj_hig_alpha2_bbh_cat8[1.0, 0.01, 10];
Mjj_hig_n2_bbh_cat8[1, 0.01, 10];
MjjHig_bbh_cat8 = RooDoubleCB(Mjj, Mjj_hig_m0_bbh_cat8, Mjj_hig_sigma_bbh_cat8, Mjj_hig_alpha1_bbh_cat8, Mjj_hig_n1_bbh_cat8, Mjj_hig_alpha2_bbh_cat8, Mjj_hig_n2_bbh_cat8);
mgg_sig_m0_cat9[125., 122, 127];
mgg_sig_sigma_cat9[1.0, 0.1, 3.0];
mgg_sig_alpha1_cat9[1.0, 0.05, 10.0];
mgg_sig_n1_cat9[2.0, 0.1, 10.0];
mgg_sig_alpha2_cat9[1.0, 0.05, 10.0];
mgg_sig_n2_cat9[2.0, 0.1, 10.0];
mggSig_cat9 = RooDoubleCB(mgg, mgg_sig_m0_cat9, mgg_sig_sigma_cat9, mgg_sig_alpha1_cat9, mgg_sig_n1_cat9, mgg_sig_alpha2_cat9, mgg_sig_n2_cat9);

mgg_hig_m0_ggh_cat9[124.2, 123, 125];
mgg_hig_sigma_ggh_cat9[2.0, 0.1, 3.0];
mgg_hig_alpha1_ggh_cat9[1.0, 0.05, 10.0];
mgg_hig_n1_ggh_cat9[2.0, 0.1, 10.0];
mgg_hig_alpha2_ggh_cat9[1.0, 0.05, 10.0];
mgg_hig_n2_ggh_cat9[2.0, 0.1, 10.0];
mggHig_ggh_cat9 = RooDoubleCB(mgg, mgg_hig_m0_ggh_cat9, mgg_hig_sigma_ggh_cat9, mgg_hig_alpha1_ggh_cat9, mgg_hig_n1_ggh_cat9, mgg_hig_alpha2_ggh_cat9, mgg_hig_n2_ggh_cat9);

mgg_hig_m0_tth_cat9[124.2, 123, 125];
mgg_hig_sigma_tth_cat9[2.0, 0.1, 3.0];
mgg_hig_alpha1_tth_cat9[1.0, 0.05, 10.0];
mgg_hig_n1_tth_cat9[2.0, 0.1, 10.0];
mgg_hig_alpha2_tth_cat9[1.0, 0.05, 10.0];
mgg_hig_n2_tth_cat9[2.0, 0.1, 10.0];
mggHig_tth_cat9 = RooDoubleCB(mgg, mgg_hig_m0_tth_cat9, mgg_hig_sigma_tth_cat9, mgg_hig_alpha1_tth_cat9, mgg_hig_n1_tth_cat9, mgg_hig_alpha2_tth_cat9, mgg_hig_n2_tth_cat9);

mgg_hig_m0_vh_cat9[124.2, 123, 125];
mgg_hig_sigma_vh_cat9[2.0, 0.1, 3.0];
mgg_hig_alpha1_vh_cat9[1.0, 0.05, 10.0];
mgg_hig_n1_vh_cat9[2.0, 0.1, 10.0];
mgg_hig_alpha2_vh_cat9[1.0, 0.05, 10.0];
mgg_hig_n2_vh_cat9[2.0, 0.1, 10.0];
mggHig_vh_cat9 = RooDoubleCB(mgg, mgg_hig_m0_vh_cat9, mgg_hig_sigma_vh_cat9, mgg_hig_alpha1_vh_cat9, mgg_hig_n1_vh_cat9, mgg_hig_alpha2_vh_cat9, mgg_hig_n2_vh_cat9);

mgg_hig_m0_qqh_cat9[124.2, 123, 125];
mgg_hig_sigma_qqh_cat9[2.0, 0.1, 3.0];
mgg_hig_alpha1_qqh_cat9[1.0, 0.05, 10.0];
mgg_hig_n1_qqh_cat9[2.0, 0.1, 10.0];
mgg_hig_alpha2_qqh_cat9[1.0, 0.05, 10.0];
mgg_hig_n2_qqh_cat9[2.0, 0.1, 10.0];
mggHig_qqh_cat9 = RooDoubleCB(mgg, mgg_hig_m0_qqh_cat9, mgg_hig_sigma_qqh_cat9, mgg_hig_alpha1_qqh_cat9, mgg_hig_n1_qqh_cat9, mgg_hig_alpha2_qqh_cat9, mgg_hig_n2_qqh_cat9);

mgg_hig_m0_bbh_cat9[124.2, 123, 125];
mgg_hig_sigma_bbh_cat9[2.0, 0.1, 3.0];
mgg_hig_alpha1_bbh_cat9[1.0, 0.05, 10.0];
mgg_hig_n1_bbh_cat9[2.0, 0.1, 10.0];
mgg_hig_alpha2_bbh_cat9[1.0, 0.05, 10.0];
mgg_hig_n2_bbh_cat9[2.0, 0.1, 10.0];
mggHig_bbh_cat9 = RooDoubleCB(mgg, mgg_hig_m0_bbh_cat9, mgg_hig_sigma_bbh_cat9, mgg_hig_alpha1_bbh_cat9, mgg_hig_n1_bbh_cat9, mgg_hig_alpha2_bbh_cat9, mgg_hig_n2_bbh_cat9);


Mjj_sig_m0_cat9[110.0, 99, 140];
Mjj_sig_sigma_cat9[20.0, 1.0, 60.0];
Mjj_sig_alpha1_cat9[1.0, 0.05, 10.0];
Mjj_sig_n1_cat9[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat9[1.0, 0.05, 10.0];
Mjj_sig_n2_cat9[2.0, 0.1, 10.0];
MjjSig_cat9 = RooDoubleCB(Mjj, Mjj_sig_m0_cat9, Mjj_sig_sigma_cat9, Mjj_sig_alpha1_cat9, Mjj_sig_n1_cat9, Mjj_sig_alpha2_cat9, Mjj_sig_n2_cat9);

Mjj_hig_par1_ggh_cat9[0.1, 0, 10];
Mjj_hig_par2_ggh_cat9[0.1, 0, 10];
Mjj_hig_par3_ggh_cat9[0.1, 0, 10];

Mjj_hig_par1_qqh_cat9[0.1, 0, 10];
Mjj_hig_par2_qqh_cat9[0.1, 0, 10];
Mjj_hig_par3_qqh_cat9[0.1, 0, 10];

Mjj_hig_m0_tth_cat9[130, 70, 190];
Mjj_hig_sigma_tth_cat9[50, 10, 100];
Mjj_hig_alpha1_tth_cat9[1.0, 0.01, 10];
Mjj_hig_n1_tth_cat9[1, 0.01, 10];
Mjj_hig_alpha2_tth_cat9[1.0, 0.01, 10];
Mjj_hig_n2_tth_cat9[1, 0.01, 10];
MjjHig_tth_cat9 = RooDoubleCB(Mjj, Mjj_hig_m0_tth_cat9, Mjj_hig_sigma_tth_cat9, Mjj_hig_alpha1_tth_cat9, Mjj_hig_n1_tth_cat9, Mjj_hig_alpha2_tth_cat9, Mjj_hig_n2_tth_cat9);

Mjj_hig_m0_vh_cat9[90, 70, 190];
Mjj_hig_sigma_vh_cat9[50, 10, 100];
Mjj_hig_alpha1_vh_cat9[1.0, 0.01, 10];
Mjj_hig_n1_vh_cat9[1, 0.01, 10];
Mjj_hig_alpha2_vh_cat9[1.0, 0.01, 10];
Mjj_hig_n2_vh_cat9[1, 0.01, 10];
MjjHig_vh_cat9 = RooDoubleCB(Mjj, Mjj_hig_m0_vh_cat9, Mjj_hig_sigma_vh_cat9, Mjj_hig_alpha1_vh_cat9, Mjj_hig_n1_vh_cat9, Mjj_hig_alpha2_vh_cat9, Mjj_hig_n2_vh_cat9);

Mjj_hig_m0_bbh_cat9[100, 10, 180];
Mjj_hig_sigma_bbh_cat9[50, 1.0, 100];
Mjj_hig_alpha1_bbh_cat9[1.0, 0.01, 10];
Mjj_hig_n1_bbh_cat9[1, 0.01, 10];
Mjj_hig_alpha2_bbh_cat9[1.0, 0.01, 10];
Mjj_hig_n2_bbh_cat9[1, 0.01, 10];
MjjHig_bbh_cat9 = RooDoubleCB(Mjj, Mjj_hig_m0_bbh_cat9, Mjj_hig_sigma_bbh_cat9, Mjj_hig_alpha1_bbh_cat9, Mjj_hig_n1_bbh_cat9, Mjj_hig_alpha2_bbh_cat9, Mjj_hig_n2_bbh_cat9);
