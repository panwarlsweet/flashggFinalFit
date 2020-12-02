MX[800,960];

MX_sig_m0_cat0[970, 960, 910];
MX_sig_sigma_cat0[25.0, 1.0, 60.0];
MX_sig_alpha1_cat0[2.0, 0.5, 4.0];
MX_sig_n1_cat0[4.0, 3, 5.0];
MX_sig_alpha2_cat0[1.0, 0.05, 10.0];
MX_sig_n2_cat0[2.0, 0.1, 10.0];
MXSig_cat0 = RooDoubleCB(MX, MX_sig_m0_cat0, MX_sig_sigma_cat0, MX_sig_alpha1_cat0, MX_sig_n1_cat0, MX_sig_alpha2_cat0, MX_sig_n2_cat0);

MX_sig_m0_cat1[970, 960, 910];
MX_sig_sigma_cat1[15.0, 5.0, 60.0];
MX_sig_alpha1_cat1[1.2,1., 4.0];
MX_sig_n1_cat1[2.0, 2, 5.0];
MX_sig_alpha2_cat1[1.0, 0.05, 10.0];
MX_sig_n2_cat1[2.0, 0.1, 10.0];
MXSig_cat1 = RooDoubleCB(MX, MX_sig_m0_cat1, MX_sig_sigma_cat1, MX_sig_alpha1_cat1, MX_sig_n1_cat1, MX_sig_alpha2_cat1, MX_sig_n2_cat1);

MX_sig_m0_cat2[970, 960, 910];
MX_sig_sigma_cat2[15.0, 7.0, 30.0];
MX_sig_alpha1_cat2[1.0, .5, 4.0];
MX_sig_n1_cat2[4.0, 3, 5.0];
MX_sig_alpha2_cat2[1.0, 0.05, 10.0];
MX_sig_n2_cat2[2.0, 0.1, 10.0];
MXSig_cat2 = RooDoubleCB(MX, MX_sig_m0_cat2, MX_sig_sigma_cat2, MX_sig_alpha1_cat2, MX_sig_n1_cat2, MX_sig_alpha2_cat2, MX_sig_n2_cat2);

MX_hig_par1_ggh_cat0[0.1, 0, 10];
MX_hig_par2_ggh_cat0[0.1, 0, 10];
MX_hig_par3_ggh_cat0[0.1, 0, 10];

MX_hig_par1_ggh_cat1[0.1, 0, 10];
MX_hig_par2_ggh_cat1[0.1, 0, 10];
MX_hig_par3_ggh_cat1[0.1, 0, 10];

MX_hig_par1_ggh_cat2[0.1, 0, 10];
MX_hig_par2_ggh_cat2[0.1, 0, 10];
MX_hig_par3_ggh_cat2[0.1, 0, 10];

MX_hig_par1_qqh_cat0[0.1, 0, 10];
MX_hig_par2_qqh_cat0[0.1, 0, 10];
MX_hig_par3_qqh_cat0[0.1, 0, 10];

MX_hig_par1_qqh_cat1[0.1, 0, 10];
MX_hig_par2_qqh_cat1[0.1, 0, 10];
MX_hig_par3_qqh_cat1[0.1, 0, 10];

MX_hig_par1_qqh_cat2[0.1, 0, 10];
MX_hig_par2_qqh_cat2[0.1, 0, 10];
MX_hig_par3_qqh_cat2[0.1, 0, 10];

MX_hig_par1_bbh_cat0[0.1, 0, 10];
MX_hig_par2_bbh_cat0[0.1, 0, 10];
MX_hig_par3_bbh_cat0[0.1, 0, 10];

MX_hig_par1_bbh_cat1[0.1, 0, 10];
MX_hig_par2_bbh_cat1[0.1, 0, 10];
MX_hig_par3_bbh_cat1[0.1, 0, 10];

MX_hig_par1_bbh_cat2[0.1, 0, 10];
MX_hig_par2_bbh_cat2[0.1, 0, 10];
MX_hig_par3_bbh_cat2[0.1, 0, 10];

MX_hig_m0_vh_cat0[91, 88, 94];
MX_hig_sigma_vh_cat0[7, 5, 10];
MX_hig_alpha_vh_cat0[-0.5, -2., .0];
MX_hig_n_vh_cat0[2.0, 0.5, 10.0];
MXHig_vh_cat0 = RooCBShape(MX, MX_hig_m0_vh_cat0, MX_hig_sigma_vh_cat0,MX_hig_alpha_vh_cat0,MX_hig_n_vh_cat0);

MX_hig_m0_vh_cat1[91, 88, 94];
MX_hig_sigma_vh_cat1[7, 5, 10];
MX_hig_alpha_vh_cat1[-0.5, -2., .0];
MX_hig_n_vh_cat1[2.0, 0.5, 10.0];
MXHig_vh_cat1 = RooCBShape(MX, MX_hig_m0_vh_cat1, MX_hig_sigma_vh_cat1,MX_hig_alpha_vh_cat1,MX_hig_n_vh_cat1);

MX_hig_m0_vh_cat2[91, 88, 94];
MX_hig_sigma_vh_cat2[7, 5, 10];
MX_hig_alpha_vh_cat2[-0.5, -2., .0];
MX_hig_n_vh_cat2[2.0, 0.5, 10.0];
MXHig_vh_cat2 = RooCBShape(MX, MX_hig_m0_vh_cat2, MX_hig_sigma_vh_cat2,MX_hig_alpha_vh_cat2,MX_hig_n_vh_cat2);

MX_hig_m0_tth_cat0[130, 110, 150];
MX_hig_sigma_tth_cat0[30, 20, 70];
MXHig_tth_cat0 = RooGaussian(MX, MX_hig_m0_tth_cat0, MX_hig_sigma_tth_cat0);

MX_hig_m0_tth_cat1[130, 110, 150];
MX_hig_sigma_tth_cat1[30, 20, 70];
MXHig_tth_cat1 = RooGaussian(MX, MX_hig_m0_tth_cat1, MX_hig_sigma_tth_cat1);

MX_hig_m0_tth_cat2[130, 110, 150];
MX_hig_sigma_tth_cat2[30, 20, 70];
MXHig_tth_cat2 = RooGaussian(MX, MX_hig_m0_tth_cat2, MX_hig_sigma_tth_cat2);
