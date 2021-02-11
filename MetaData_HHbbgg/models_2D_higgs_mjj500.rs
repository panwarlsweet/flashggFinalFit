Mjj[200,560];

Mjj_sig_m0_cat0[450, 420, 510];
Mjj_sig_sigma_cat0[10.0, 1.0, 60.0];
Mjj_sig_alpha1_cat0[1.0,0.05, 4.0];
Mjj_sig_n1_cat0[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat0[1.0, 0.05, 10.0];
Mjj_sig_n2_cat0[2.0, 0.1, 10.0];
MjjSig_cat0 = RooDoubleCB(Mjj, Mjj_sig_m0_cat0, Mjj_sig_sigma_cat0, Mjj_sig_alpha1_cat0, Mjj_sig_n1_cat0, Mjj_sig_alpha2_cat0, Mjj_sig_n2_cat0);

Mjj_sig_m0_cat1[450, 420, 510];
Mjj_sig_sigma_cat1[10.0, 1.0, 60.0];
Mjj_sig_alpha1_cat1[1.0,0.05, 4.0];
Mjj_sig_n1_cat1[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat1[1.0, 0.05, 10.0];
Mjj_sig_n2_cat1[2.0, 0.1, 10.0];
MjjSig_cat1 = RooDoubleCB(Mjj, Mjj_sig_m0_cat1, Mjj_sig_sigma_cat1, Mjj_sig_alpha1_cat1, Mjj_sig_n1_cat1, Mjj_sig_alpha2_cat1, Mjj_sig_n2_cat1);

Mjj_sig_m0_cat2[450, 420, 510];
Mjj_sig_sigma_cat2[10.0, 1.0, 60.0];
Mjj_sig_alpha1_cat2[1.0,0.05, 4.0];
Mjj_sig_n1_cat2[2.0, 0.1, 10.0];
Mjj_sig_alpha2_cat2[1.0, 0.05, 10.0];
Mjj_sig_n2_cat2[2.0, 0.1, 10.0];
MjjSig_cat2 = RooDoubleCB(Mjj, Mjj_sig_m0_cat2, Mjj_sig_sigma_cat2, Mjj_sig_alpha1_cat2, Mjj_sig_n1_cat2, Mjj_sig_alpha2_cat2, Mjj_sig_n2_cat2);

Mjj_hig_par1_ggh_cat0[0.1, 0, 10];
Mjj_hig_par2_ggh_cat0[0.1, 0, 10];
Mjj_hig_par3_ggh_cat0[0.1, 0, 10];

Mjj_hig_par1_ggh_cat1[0.1, 0, 10];
Mjj_hig_par2_ggh_cat1[0.1, 0, 10];
Mjj_hig_par3_ggh_cat1[0.1, 0, 10];

Mjj_hig_par1_ggh_cat2[0.1, 0, 10];
Mjj_hig_par2_ggh_cat2[0.1, 0, 10];
Mjj_hig_par3_ggh_cat2[0.1, 0, 10];

Mjj_hig_par1_qqh_cat0[0.1, 0, 10];
Mjj_hig_par2_qqh_cat0[0.1, 0, 10];
Mjj_hig_par3_qqh_cat0[0.1, 0, 10];

Mjj_hig_par1_qqh_cat1[0.1, 0, 10];
Mjj_hig_par2_qqh_cat1[0.1, 0, 10];
Mjj_hig_par3_qqh_cat1[0.1, 0, 10];

Mjj_hig_par1_qqh_cat2[0.1, 0, 10];
Mjj_hig_par2_qqh_cat2[0.1, 0, 10];
Mjj_hig_par3_qqh_cat2[0.1, 0, 10];

Mjj_hig_par1_bbhyb2_cat0[0.1, 0, 10];
Mjj_hig_par2_bbhyb2_cat0[0.1, 0, 10];
Mjj_hig_par3_bbhyb2_cat0[0.1, 0, 10];

Mjj_hig_par1_bbhyb2_cat1[0.1, 0, 10];
Mjj_hig_par2_bbhyb2_cat1[0.1, 0, 10];
Mjj_hig_par3_bbhyb2_cat1[0.1, 0, 10];

Mjj_hig_par1_bbhyb2_cat2[0.1, 0, 10];
Mjj_hig_par2_bbhyb2_cat2[0.1, 0, 10];
Mjj_hig_par3_bbhyb2_cat2[0.1, 0, 10];

Mjj_hig_par1_bbhybyt_cat0[0.1, 0, 10];
Mjj_hig_par2_bbhybyt_cat0[0.1, 0, 10];
Mjj_hig_par3_bbhybyt_cat0[0.1, 0, 10];

Mjj_hig_par1_bbhybyt_cat1[0.1, 0, 10];
Mjj_hig_par2_bbhybyt_cat1[0.1, 0, 10];
Mjj_hig_par3_bbhybyt_cat1[0.1, 0, 10];

Mjj_hig_par1_bbhybyt_cat2[0.1, 0, 10];
Mjj_hig_par2_bbhybyt_cat2[0.1, 0, 10];
Mjj_hig_par3_bbhybyt_cat2[0.1, 0, 10];

Mjj_hig_m0_vh_cat0[91, 88, 94];
Mjj_hig_sigma_vh_cat0[7, 5, 10];
Mjj_hig_alpha_vh_cat0[-0.5, -2., .0];
Mjj_hig_n_vh_cat0[2.0, 0.5, 10.0];
MjjHig_vh_cat0 = RooCBShape(Mjj, Mjj_hig_m0_vh_cat0, Mjj_hig_sigma_vh_cat0,Mjj_hig_alpha_vh_cat0,Mjj_hig_n_vh_cat0);

Mjj_hig_m0_vh_cat1[91, 88, 94];
Mjj_hig_sigma_vh_cat1[7, 5, 10];
Mjj_hig_alpha_vh_cat1[-0.5, -2., .0];
Mjj_hig_n_vh_cat1[2.0, 0.5, 10.0];
MjjHig_vh_cat1 = RooCBShape(Mjj, Mjj_hig_m0_vh_cat1, Mjj_hig_sigma_vh_cat1,Mjj_hig_alpha_vh_cat1,Mjj_hig_n_vh_cat1);

Mjj_hig_m0_vh_cat2[91, 88, 94];
Mjj_hig_sigma_vh_cat2[7, 5, 10];
Mjj_hig_alpha_vh_cat2[-0.5, -2., .0];
Mjj_hig_n_vh_cat2[2.0, 0.5, 10.0];
MjjHig_vh_cat2 = RooCBShape(Mjj, Mjj_hig_m0_vh_cat2, Mjj_hig_sigma_vh_cat2,Mjj_hig_alpha_vh_cat2,Mjj_hig_n_vh_cat2);

Mjj_hig_m0_tth_cat0[130, 110, 150];
Mjj_hig_sigma_tth_cat0[30, 20, 70];
MjjHig_tth_cat0 = RooGaussian(Mjj, Mjj_hig_m0_tth_cat0, Mjj_hig_sigma_tth_cat0);

Mjj_hig_m0_tth_cat1[130, 110, 150];
Mjj_hig_sigma_tth_cat1[30, 20, 70];
MjjHig_tth_cat1 = RooGaussian(Mjj, Mjj_hig_m0_tth_cat1, Mjj_hig_sigma_tth_cat1);

Mjj_hig_m0_tth_cat2[130, 110, 150];
Mjj_hig_sigma_tth_cat2[30, 20, 70];
MjjHig_tth_cat2 = RooGaussian(Mjj, Mjj_hig_m0_tth_cat2, Mjj_hig_sigma_tth_cat2);
