# SFX (Sound Effects)

Example (bes1gcw.sfx):
```sfx
///////////////////////////////////
// Common to Worlds -------------------------------------------------------------------------------------------------
..\..\global\effects\eng_chop_a_loop.wav -resample pc 22050
// Unit Weapons -----------------------------------------------------------------------------------------------------
// Common Unit Weapons
..\..\global\effects\emt_steam_lp.wav -resample pc 22050
// Common Props and Effects -------------------------------------------------------------------------------------
..\..\global\effects\wpn_powerDispense_pickUp.wav   -resample pc 22050
..\..\global\effects\ifc_NoAmmo.wav                 -resample pc 22050
..\..\global\effects\fusioncutter.wav               wpn_fusionCutter_lp   -resample pc 22050
..\..\global\effects\wpn_reconDroid_Launch.wav      -resample pc 22050
..\..\global\effects\mineactivate2.wav               -resample pc 22050
..\..\global\effects\wpn_energyRecharge.wav         -resample pc 22050
..\..\global\effects\wpn_energyDepleted.wav         -resample pc 22050
#ifplatform pc
..\..\global\effects\emt_torch_lp.wav                 -resample pc 44100
..\..\global\effects\wpn_powerDispenser.wav           -resample pc 22050
..\..\global\effects\wpn_lightsaber_idle_lp.wav       -resample pc 22050
..\..\global\effects\wpn_lightsaber_swing_01.wav      -resample pc 22050
..\..\global\effects\wpn_lightsaber_swing_02.wav      -resample pc 22050
..\..\global\effects\wpn_lightsaber_swing_03.wav      -resample pc 22050
..\..\global\effects\wpn_sniperRifle_zoomIn01.wav     -resample pc 22050
..\..\global\effects\wpn_sniperRifle_zoomIn02.wav     -resample pc 22050
..\..\global\effects\wpn_sniperRifle_zoomOut.wav      -resample pc 22050
//..\..\global\effects\wpn_intrcptTnk_trtYaw_st.wav    -resample pc 22050
//..\..\global\effects\wpn_intrcptTnk_trtYaw_end.wav   -resample pc 22050
..\..\global\effects\wpn_intrcptTnk_trtYaw_lp.wav     -resample pc 22050
..\..\global\effects\wpn_intrcptTnk_trtPtch_lp.wav    -resample pc 22050
#endifplatform pc

// --------------------------------------------------------------------------------------------------------------

// Command Posts ------------------------------------------------------------------------------------------------
..\..\global\effects\com_blg_commandpost_capture.wav        
..\..\global\effects\com_blg_commandpost_charge.wav         -resample pc 22050
..\..\global\effects\com_blg_commandpost_discharge.wav      -resample pc 22050
..\..\global\effects\com_blg_commandpost_dispute.wav
..\..\global\effects\com_blg_commandpost_lost.wav           
..\..\global\effects\com_blg_commandpost1.wav
..\..\global\effects\com_blg_commandpost2.wav
..\..\global\effects\com_blg_commandpost3.wav
// ---------------------------------------------------------------------------------------------------------------

// Ammo Droid Gonk -----------------------------------------------------------------------------------------------
#ifplatform pc
..\..\global\effects\droid_gonk_01.wav          -resample pc 22050
..\..\global\effects\droid_gonk_02.wav          -resample pc 22050
..\..\global\effects\droid_gonk_03.wav          -resample pc 22050
..\..\global\effects\droid_gonk_04.wav          -resample pc 22050
//..\..\global\effects\droid_gonk_die_01.wav      -resample pc 22050
//..\..\global\effects\droid_gonk_die_02.wav      -resample pc 22050
#endifplatform pc

// ----------------------------------------------------------------------------------------------------------

// Medical Droid FX7 ----------------------------------------------------------------------------------------
..\..\global\effects\crt_medicalDroid04.wav  -resample pc 22050
#ifplatform pc
..\..\global\effects\droid_fx7_chatter_04.wav     -resample pc 22050
..\..\global\effects\droid_fx7_chatter_01.wav     -resample pc 22050
..\..\global\effects\droid_fx7_chatter_02.wav     -resample pc 22050
..\..\global\effects\droid_fx7_chatter_03.wav     -resample pc 22050
//..\..\global\effects\droid_fx7_hum_lp.wav         -resample pc 22050
..\..\global\effects\droid_fx7_recharge_01.wav    -resample pc 16000
..\..\global\effects\droid_fx7_recharge_02.wav    -resample pc 16000
..\..\global\effects\droid_fx7_recharge_03.wav    -resample pc 16000
..\..\global\effects\droid_fx7_recharge_04.wav    -resample pc 16000
//..\..\global\effects\droid_fx7death.wav           -resample pc 22050
#endifplatform pc

// --------------------------------------------------------------------------------------------------------------

// Vehicle Repair Droid R5D4 ------------------------------------------------------------------------------------
#ifplatform pc
..\..\global\effects\droid_r5_chatter_01.wav    -resample pc 22050
..\..\global\effects\droid_r5_chatter_02.wav    -resample pc 22050
..\..\global\effects\droid_r5_chatter_03.wav    -resample pc 22050
..\..\global\effects\droid_r5_chatter_04.wav    -resample pc 22050
..\..\global\effects\droid_r5_chatter_05.wav    -resample pc 22050
//..\..\global\effects\droid_r5_death.wav         -resample pc 22050
#endifplatform pc

// --------------------------------------------------------------------------------------------------------------

// Ordnance Hums ---------------------------------------------------------------------------------------------------------
// ----- High hum hums for unit blasters -----
#ifplatform pc
..\..\global\effects\ammo_blaster_lp01.wav   -resample pc 22050
..\..\global\effects\ammo_blaster_lp04.wav   -resample pc 22050
#endifplatform pc


// ----- Low hums for turret blasters -----
#ifplatform pc
..\..\global\effects\ammo_blaster_lp02.wav   -resample pc 22050
..\..\global\effects\ammo_blaster_lp03.wav   -resample pc 22050
#endifplatform pc


// ----- Rocket hum-thrust -----
#ifplatform pc
..\..\global\effects\ammo_rocket_lp02.wav    -resample pc 22050
..\..\global\effects\ammo_rocket_lp03.wav    -resample pc 22050
..\..\global\effects\ammo_rocket_lp05.wav    -resample pc 22050
..\..\global\effects\ammo_rocket_lp06.wav    -resample pc 22050
#endifplatform pc

// -----------------------------------------------------------------------------------------------------------------------

// Laser Impact ------------------------------------------------------------------------------------------
#ifplatform pc
..\..\global\effects\imp_laser_dirt_07.wav      -resample pc 22050
..\..\global\effects\imp_laser_dirt_09.wav      -resample pc 22050
..\..\global\effects\imp_laser_stone_03.wav     -resample pc 22050
..\..\global\effects\imp_laser_stone_04.wav     -resample pc 22050
..\..\global\effects\imp_laser_stone_05.wav     -resample pc 22050
..\..\global\effects\imp_laser_metal_02.wav     -resample pc 22050
..\..\global\effects\imp_laser_metal_03.wav     -resample pc 22050
..\..\global\effects\imp_laser_metal_05.wav     -resample pc 22050
..\..\global\effects\imp_laser_metal_06.wav     -resample pc 22050
..\..\global\effects\imp_laser_metal_07.wav     -resample pc 22050
..\..\global\effects\imp_laser_metal_08.wav     -resample pc 22050
..\..\global\effects\imp_laser_metal_09.wav     -resample pc 22050
..\..\global\effects\imp_laser_metal_16.wav     -resample pc 22050
..\..\global\effects\imp_laser_metal_18.wav     -resample pc 22050
..\..\global\effects\imp_laser_metal_21.wav     -resample pc 22050
..\..\global\effects\imp_ricco_02.wav           -resample pc 22050
..\..\global\effects\imp_ricco_03.wav           -resample pc 22050
..\..\global\effects\imp_ricco_04.wav           -resample pc 22050
..\..\global\effects\imp_ricco_06.wav           -resample pc 22050
..\..\global\effects\imp_ricco_08.wav           -resample pc 22050
..\..\global\effects\imp_ricco_12.wav           -resample pc 22050
#endifplatform pc

// ---------------------------------------------------------------------------------------------------

// Generic Throw ---------------------------------------------------------------------------------------------------------
..\..\global\effects\wpn_throw01.wav     -resample pc 22050
..\..\global\effects\wpn_throw02.wav     -resample pc 22050
..\..\global\effects\wpn_throw03.wav     -resample pc 22050
..\..\global\effects\wpn_throw04.wav     -resample pc 22050
..\..\global\effects\wpn_throw05.wav     -resample pc 22050
#ifplatform pc
//..\..\global\effects\wpn_thermalDetonator_throw.wav      -resample pc 22050
#endifplatform pc

// -----------------------------------------------------------------------------------------------------------------------

// Grenade Bounce --------------------------------------------------------------------------------------------------------
..\..\global\effects\imp_grenade_dirt_01.wav    -resample pc 22050
..\..\global\effects\imp_grenade_dirt_03.wav    -resample pc 22050
..\..\global\effects\imp_grenade_dirt_04.wav    -resample pc 22050
..\..\global\effects\imp_grenade_stone_01.wav   -resample pc 22050
..\..\global\effects\imp_grenade_stone_03.wav   -resample pc 22050
..\..\global\effects\imp_grenade_stone_04.wav   -resample pc 22050
..\..\global\effects\imp_grenade_wood_03b.wav   -resample pc 22050
// -----------------------------------------------------------------------------------------------------------------------

// Concussion Grenade Explosion -----------------------------------------------------------------------------------------
#ifplatform pc
..\..\global\effects\exp_ord_grenade02.wav             -resample pc 44100
..\..\global\effects\exp_ord_grenade03.wav             -resample pc 44100
..\..\global\effects\exp_ord_grenade01.wav             -resample pc 44100
..\..\global\effects\exp_ord_rocket_small01.wav        -resample pc 44100
..\..\global\effects\exp_ord_rocket_small02.wav        -resample pc 44100
..\..\global\effects\exp_ord_rocket_small03.wav        -resample pc 44100
#endifplatform pc

//---------------------------------------------------------------------------------------------------------------------

// Thermal Detonator Explosion ----------------------------------------------------------------------------------------
#ifplatform pc
..\..\global\effects\exp_ord_thermalDetonator01.wav    -resample pc 44100
..\..\global\effects\exp_ord_thermalDetonator02.wav    -resample pc 44100
#endifplatform pc

//---------------------------------------------------------------------------------------------------------------------

// Rocket Explosion ---------------------------------------------------------------------------------------------------
#ifplatform pc
..\..\global\effects\exp_ord_rocket_large01.wav        -resample pc 44100
..\..\global\effects\exp_ord_rocket_large02.wav        -resample pc 44100
..\..\global\effects\exp_ord_rocket_large03.wav        -resample pc 44100
..\..\global\effects\exp_ord_rocket_med01.wav          -resample pc 44100
..\..\global\effects\exp_ord_rocket_med02.wav          -resample pc 44100
..\..\global\effects\exp_ord_rocket_med03.wav          -resample pc 44100
#endifplatform pc

// ----- Jetpack -----
..\..\global\effects\rep_inf_jetpack.wav             
..\..\global\effects\rep_weap_jetpack_turnon.wav     
..\..\global\effects\rep_weap_jetpack_turnoff.wav    
//-----------------------------------------------------------------------------------------------------------------------

// Weapon Foley ----------------------------------------------------------------------------------------------------------
// Common Weapon Foley
#ifplatform pc
..\..\global\effects\mvt_getup_rifle.wav     -resample pc 22050
..\..\global\effects\mvt_jump_rifle.wav      -resample pc 22050
..\..\global\effects\mvt_land_rifle.wav      -resample pc 22050
..\..\global\effects\mvt_squat_rifle.wav     -resample pc 22050
..\..\global\effects\mvt_roll_rifle.wav      -resample pc 22050
..\..\global\effects\mvt_lie_rifle.wav       -resample pc 22050
..\..\global\effects\mvt_stop_rifle.wav      -resample pc 22050
..\..\global\effects\mvt_getup_pistol.wav    -resample pc 22050
..\..\global\effects\mvt_jump_pistol.wav     -resample pc 22050
..\..\global\effects\mvt_land_pistol.wav     -resample pc 22050
..\..\global\effects\mvt_squat_pistol.wav    -resample pc 22050
..\..\global\effects\mvt_roll_pistol.wav     -resample pc 22050
..\..\global\effects\mvt_lie_pistol.wav      -resample pc 22050
..\..\global\effects\mvt_stop_pistol.wav     -resample pc 22050
..\..\global\effects\mvt_getup_bazooka.wav   -resample pc 22050
..\..\global\effects\mvt_jump_bazooka.wav    -resample pc 22050
..\..\global\effects\mvt_land_bazooka.wav    -resample pc 22050
..\..\global\effects\mvt_squat_bazooka.wav   -resample pc 22050
..\..\global\effects\mvt_roll_bazooka.wav    -resample pc 22050
..\..\global\effects\mvt_lie_bazooka.wav     -resample pc 22050
..\..\global\effects\mvt_stop_bazooka.wav    -resample pc 22050
..\..\global\effects\mvt_bazooka_lgBF_01.wav -resample pc 22050
..\..\global\effects\mvt_bazooka_lgBF_02.wav -resample pc 22050 
..\..\global\effects\mvt_bazooka_lgBF_03.wav -resample pc 22050
..\..\global\effects\mvt_bazooka_smBF.wav    -resample pc 22050
#endifplatform pc

// ---------------------------------------------------------------------------------------------------------------------


/////// Common to Planet /////// ---------------------------------------------------------------------------------------

/////// Common to Map /////// -----------------------------------------------------------------------------------


/////// Common to Era ///////// -------------------------------------------------------------------------------------------

// Object Explosions ---------------------------------------------------------------------------------------------

// ----- Medium ----- Orbital Strike Combatspeeder Fightertank
#ifplatform pc
..\..\global\effects\exp_obj_med05.wav            -resample pc 44100
..\..\global\effects\exp_obj_med04.wav            -resample pc 44100
..\..\global\effects\exp_obj_med03.wav            -resample pc 44100
..\..\global\effects\exp_obj_med02.wav            -resample pc 44100
..\..\global\effects\exp_obj_med01.wav            -resample pc 44100
..\..\global\effects\exp_distant_medium01.wav     -resample pc 22050
..\..\global\effects\exp_distant_medium02.wav     -resample pc 22050
..\..\global\effects\exp_verydistant_medium01.wav -resample pc 320
..\..\global\effects\exp_verydistant_medium02.wav -resample pc 320
#endifplatform pc

// ----- Small ------ STAP Speederbike GunTurrets Droideka Large Blaster Ordnance
#ifplatform pc
..\..\global\effects\exp_obj_small01.wav          -resample pc 44100
..\..\global\effects\exp_obj_small02.wav          -resample pc 44100
..\..\global\effects\exp_obj_small03.wav          -resample pc 44100
..\..\global\effects\exp_obj_small04.wav          -resample pc 44100
..\..\global\effects\exp_obj_small05.wav          -resample pc 44100
..\..\global\effects\exp_distant_small02.wav      -resample pc 22050
..\..\global\effects\exp_distant_small01.wav      -resample pc 22050
..\..\global\effects\exp_verydistant_small01.wav  -resample pc 320
..\..\global\effects\exp_verydistant_small02.wav  -resample pc 320
#endifplatform pc

// --------------------------------------------------------------------------------------------------------------

// Sub Explosions ------------------------------------------------------------------------------------------------
// ----- Pop -----
#ifplatform pc
..\..\global\effects\exp_sub01.wav      -resample pc 22050
..\..\global\effects\exp_sub02.wav      -resample pc 22050
..\..\global\effects\exp_sub03.wav      -resample pc 22050
#endifplatform pc


// ----- Hiss -----
#ifplatform pc
//..\..\global\effects\exp_sub04.wav      -resample pc 22050
#endifplatform pc


// ----- Pop and Hiss -----
#ifplatform pc
..\..\global\effects\exp_sub05.wav      -resample pc 22050
..\..\global\effects\exp_sub06.wav      -resample pc 22050
..\..\global\effects\exp_sub07.wav      -resample pc 22050
..\..\global\effects\exp_sub08.wav      -resample pc 22050
#endifplatform pc

// -------------------------------------------------------------------------------------------------------------


// ----- Alliance Unit Weapons ------------------------------------------------------------------------
#ifplatform pc
..\..\gcw\effects\wpn_all_blaster_fire.wav      -resample pc 44100
..\..\gcw\effects\wpn_all_pistol_fire.wav       -resample pc 44100
..\..\gcw\effects\wpn_all_torplauncher_fire.wav -resample pc 44100
..\..\gcw\effects\wpn_all_bowcaster_fire.wav    -resample pc 44100
..\..\gcw\effects\wpn_bowcaster_chargeup.wav    -resample pc 44100
..\..\gcw\effects\wpn_all_sniperrifle_fire.wav  -resample pc 44100
#endifplatform pc


// ----- Imperial Unit Weapons ------------------------------------------------------------------------
#ifplatform pc
..\..\gcw\effects\wpn_imp_blaster_fire.wav      -resample pc 44100
..\..\gcw\effects\wpn_imp_pistol_fire.wav       -resample pc 44100
..\..\gcw\effects\wpn_imp_sniperrifle_fire.wav  -resample pc 44100
..\..\gcw\effects\wpn_imp_mortar_fire.wav       -resample pc 44100
#endifplatform pc


// GCW Unit Weapons ------------------------------------------------------------------------------------------
#ifplatform pc
..\..\gcw\effects\wpn_all_unit_lockon_lp.wav     -resample pc 22050
//..\..\gcw\effects\wpn_all_vehicle_lockon_lp.wav  -resample pc 22050
..\..\gcw\effects\wpn_imp_unit_lockon_lp.wav     -resample pc 22050
//..\..\gcw\effects\wpn_imp_vehicle_lockon_lp.wav  -resample pc 22050
..\..\gcw\effects\crtr_vader_breath_lp.wav       -resample pc 22050
#endifplatform pc


// ----- GCW Equip --------------------------------------------------------------------------------------------
#ifplatform pc
..\..\gcw\effects\wpn_rebel_lgEquip.wav       -resample pc 22050
..\..\gcw\effects\wpn_rebel_medEquip.wav      -resample pc 22050
..\..\gcw\effects\wpn_rebel_smlEquip.wav      -resample pc 22050
..\..\gcw\effects\wpn_empire_lgEquip.wav      -resample pc 22050
..\..\gcw\effects\wpn_empire_medEquip.wav     -resample pc 22050
..\..\gcw\effects\wpn_empire_smlEquip.wav     -resample pc 22050
#endifplatform pc


// ----- GCW Reload --------------------------------------------------------------------------------------------
#ifplatform pc
..\..\gcw\effects\wpn_rebel_medReload.wav    -resample pc 22050
..\..\gcw\effects\wpn_rebel_lgReload.wav     -resample pc 22050
..\..\gcw\effects\wpn_empire_medReload.wav   -resample pc 22050
..\..\gcw\effects\wpn_empire_lgReload.wav    -resample pc 22050
#endifplatform pc

// --------------------------------------------------------------------------------------------------------------

// ----- Imperial Sith Probe Droid Ordnance -----
#ifplatform pc
..\..\global\effects\droid_probe_beeps_01.wav   -resample pc 22050
..\..\global\effects\droid_probe_beeps_02.wav   -resample pc 22050
..\..\global\effects\droid_probe_beeps_03.wav   -resample pc 22050
..\..\global\effects\droid_probe_beeps_04.wav   -resample pc 22050
..\..\global\effects\droid_probe_beeps_05.wav   -resample pc 22050
..\..\global\effects\droid_probe_eng_lp.wav     -resample pc 22050
#endifplatform pc

// -------------------------------------------------------------------------------------------------------------------

// Unit Pain Chatter VO -----------------------------------------------------------------------------------------

// ----- Alliance -----
..\..\gcw\effects\AICOM401.wav -resample pc 22050
..\..\gcw\effects\AICOM402.wav -resample pc 22050
..\..\gcw\effects\AICOM403.wav -resample pc 22050
..\..\gcw\effects\AICOM404.wav -resample pc 22050
..\..\gcw\effects\AICOM405.wav -resample pc 22050
..\..\gcw\effects\AICOM406.wav -resample pc 22050

// ----- Imperial -----
..\..\gcw\effects\IICOM416.wav -resample pc 22050
..\..\gcw\effects\IICOM417.wav -resample pc 22050
..\..\gcw\effects\IICOM418.wav -resample pc 22050
..\..\gcw\effects\IICOM419.wav -resample pc 22050
..\..\gcw\effects\IICOM420.wav -resample pc 22050
..\..\gcw\effects\IICOM421.wav -resample pc 22050


// ----- Wookiee Chatter ---------------------------------------------------------------------------
#ifplatform pc
..\..\global\effects\crtr_wookiee_chatter_01.wav     -resample pc 22050
..\..\global\effects\crtr_wookiee_chatter_02.wav     -resample pc 22050
..\..\global\effects\crtr_wookiee_chatter_03.wav     -resample pc 22050
..\..\global\effects\crtr_wookiee_chatter_05.wav     -resample pc 22050
..\..\global\effects\crtr_wookiee_chatter_06.wav     -resample pc 22050
..\..\global\effects\crtr_wookiee_death.wav          -resample pc 22050
..\..\global\effects\crtr_wookiee_hurt.wav           -resample pc 22050
#endifplatform pc


/////// Common to Units --------------------------------------------------------------------------------------------------


/////// Common to Vehicles ///////// -------------------------------------------------------------------------------------

// Vehicle Equip
..\..\global\effects\wpn_vehicle_weaponEquip.wav     -resample pc 22050

/////// Map Specific ///////// --------------------------------------------------------------------------------------------


// ----- ATST Weapons --------------------------------------------------------------------------------------
#ifplatform pc
..\..\gcw\effects\wpn_atst_headBlaster_fire.wav     -resample pc 44100
#endifplatform pc

// ---------------------------------------------------------------------------------------------------------

// Trooper Foley Effects -------------------------------------------------------
// Terrain Independent Foley
#ifplatform pc
..\..\global\effects\mvt_trooper_squat.wav          -resample pc 22050
#endifplatform pc


//-- Metal - Walkways etc.
#ifplatform pc
..\..\global\effects\mvt_trooper_getup_Metal.wav         -resample pc 22050
..\..\global\effects\mvt_trooper_jump_Metal.wav          -resample pc 22050
..\..\global\effects\mvt_trooper_land_Metal.wav          -resample pc 22050
..\..\global\effects\mvt_trooper_Metal_lgBF_01.wav       -resample pc 22050
..\..\global\effects\mvt_trooper_Metal_lgBF_02.wav       -resample pc 22050
..\..\global\effects\mvt_trooper_Metal_lgBF_03.wav       -resample pc 22050
..\..\global\effects\mvt_trooper_Metal_smBF.wav          -resample pc 22050
..\..\global\effects\mvt_trooper_lie_Metal.wav           -resample pc 22050
..\..\global\effects\mvt_trooper_roll_Metal.wav          -resample pc 22050
..\..\global\effects\mvt_trooper_run_Metal_L01.wav       -resample pc 22050
..\..\global\effects\mvt_trooper_run_Metal_L02.wav       -resample pc 22050
..\..\global\effects\mvt_trooper_run_Metal_L03.wav       -resample pc 22050
..\..\global\effects\mvt_trooper_run_Metal_L04.wav       -resample pc 22050
..\..\global\effects\mvt_trooper_run_Metal_R01.wav       -resample pc 22050
..\..\global\effects\mvt_trooper_run_Metal_R02.wav       -resample pc 22050
..\..\global\effects\mvt_trooper_run_Metal_R03.wav       -resample pc 22050
..\..\global\effects\mvt_trooper_run_Metal_R04.wav       -resample pc 22050
..\..\global\effects\mvt_trooper_walk_Metal_L01.wav      -resample pc 22050
..\..\global\effects\mvt_trooper_walk_Metal_L02.wav      -resample pc 22050
..\..\global\effects\mvt_trooper_walk_Metal_L03.wav      -resample pc 22050
..\..\global\effects\mvt_trooper_walk_Metal_L04.wav      -resample pc 22050
..\..\global\effects\mvt_trooper_walk_Metal_R01.wav      -resample pc 22050
..\..\global\effects\mvt_trooper_walk_Metal_R02.wav      -resample pc 22050
..\..\global\effects\mvt_trooper_walk_Metal_R03.wav      -resample pc 22050
..\..\global\effects\mvt_trooper_walk_Metal_R04.wav      -resample pc 22050
..\..\global\effects\mvt_trooper_stop_Metal.wav          -resample pc 22050
#endifplatform pc


// Soldier Foley Effects --------------------------------------------------------------------------------------------------
// Terrain Independent Foley
#ifplatform pc
..\..\gcw\effects\mvt_Soldier_squat.wav       -resample pc 22050
#endifplatform pc



//-- Metal - Walkways etc.
#ifplatform pc
..\..\gcw\effects\mvt_Soldier_getup_Metal.wav         -resample pc 22050
..\..\gcw\effects\mvt_Soldier_jump_Metal.wav          -resample pc 22050
..\..\gcw\effects\mvt_Soldier_land_Metal.wav          -resample pc 22050
..\..\gcw\effects\mvt_Soldier_Metal_lgBF_01.wav       -resample pc 22050
..\..\gcw\effects\mvt_Soldier_Metal_lgBF_02.wav       -resample pc 22050
..\..\gcw\effects\mvt_Soldier_Metal_smBF.wav          -resample pc 22050
..\..\gcw\effects\mvt_Soldier_lie_Metal.wav           -resample pc 22050
..\..\gcw\effects\mvt_Soldier_roll_Metal.wav          -resample pc 22050
..\..\gcw\effects\mvt_Soldier_run_Metal_L01.wav       -resample pc 22050
..\..\gcw\effects\mvt_Soldier_run_Metal_L02.wav       -resample pc 22050
..\..\gcw\effects\mvt_Soldier_run_Metal_L03.wav       -resample pc 22050
..\..\gcw\effects\mvt_Soldier_run_Metal_L04.wav       -resample pc 22050
..\..\gcw\effects\mvt_Soldier_run_Metal_R01.wav       -resample pc 22050
..\..\gcw\effects\mvt_Soldier_run_Metal_R02.wav       -resample pc 22050
..\..\gcw\effects\mvt_Soldier_run_Metal_R03.wav       -resample pc 22050
..\..\gcw\effects\mvt_Soldier_run_Metal_R04.wav       -resample pc 22050
..\..\gcw\effects\mvt_Soldier_walk_Metal_L01.wav      -resample pc 22050
..\..\gcw\effects\mvt_Soldier_walk_Metal_L02.wav      -resample pc 22050
..\..\gcw\effects\mvt_Soldier_walk_Metal_L03.wav      -resample pc 22050
..\..\gcw\effects\mvt_Soldier_walk_Metal_L04.wav      -resample pc 22050
..\..\gcw\effects\mvt_Soldier_walk_Metal_R01.wav      -resample pc 22050
..\..\gcw\effects\mvt_Soldier_walk_Metal_R02.wav      -resample pc 22050
..\..\gcw\effects\mvt_Soldier_walk_Metal_R03.wav      -resample pc 22050
..\..\gcw\effects\mvt_Soldier_walk_Metal_R04.wav      -resample pc 22050
..\..\gcw\effects\mvt_Soldier_stop_Metal.wav          -resample pc 22050
#endifplatform pc


// Wookiee Foley Effects --------------------------------------------------------------------------------------------------
// Terrain Independent Foley
#ifplatform pc
..\..\global\effects\mvt_Wookiee_squat.wav       -resample pc 22050
#endifplatform pc



//-- Metal - Walkways etc.
#ifplatform pc
..\..\global\effects\mvt_Wookiee_getup_Metal.wav         -resample pc 22050
..\..\global\effects\mvt_Wookiee_jump_Metal.wav          -resample pc 22050
..\..\global\effects\mvt_Wookiee_land_Metal.wav          -resample pc 22050
..\..\global\effects\mvt_wookiee_Metal_lgBF_01.wav       -resample pc 22050
..\..\global\effects\mvt_wookiee_Metal_lgBF_02.wav       -resample pc 22050
..\..\global\effects\mvt_wookiee_Metal_smBF.wav          -resample pc 22050
..\..\global\effects\mvt_Wookiee_lie_Metal.wav           -resample pc 22050
..\..\global\effects\mvt_Wookiee_roll_Metal.wav          -resample pc 22050
..\..\global\effects\mvt_Wookiee_run_Metal_L01.wav       -resample pc 22050
..\..\global\effects\mvt_Wookiee_run_Metal_L02.wav       -resample pc 22050
..\..\global\effects\mvt_Wookiee_run_Metal_L03.wav       -resample pc 22050
..\..\global\effects\mvt_Wookiee_run_Metal_L04.wav       -resample pc 22050
..\..\global\effects\mvt_Wookiee_run_Metal_R01.wav       -resample pc 22050
..\..\global\effects\mvt_Wookiee_run_Metal_R02.wav       -resample pc 22050
..\..\global\effects\mvt_Wookiee_run_Metal_R03.wav       -resample pc 22050
..\..\global\effects\mvt_Wookiee_run_Metal_R04.wav       -resample pc 22050
..\..\global\effects\mvt_Wookiee_walk_Metal_L01.wav      -resample pc 22050
..\..\global\effects\mvt_Wookiee_walk_Metal_L02.wav      -resample pc 22050
..\..\global\effects\mvt_Wookiee_walk_Metal_L03.wav      -resample pc 22050
..\..\global\effects\mvt_Wookiee_walk_Metal_L04.wav      -resample pc 22050
..\..\global\effects\mvt_Wookiee_walk_Metal_R01.wav      -resample pc 22050
..\..\global\effects\mvt_Wookiee_walk_Metal_R02.wav      -resample pc 22050
..\..\global\effects\mvt_Wookiee_walk_Metal_R03.wav      -resample pc 22050
..\..\global\effects\mvt_Wookiee_walk_Metal_R04.wav      -resample pc 22050
..\..\global\effects\mvt_Wookiee_stop_Metal.wav          -resample pc 22050
#endifplatform pc



// Bespin Cloud Car --------------------------------------------------------------------------------------------
#ifplatform pc
..\..\cw\effects\wpn_gunship_rocket_fire.wav      -resample pc 44100
effects\wpn_cloudCar_blaster_fire.wav    -resample pc 44100
effects\eng_cloudCar_low_lp.wav          -resample pc 22050
effects\eng_cloudCar_mid_lp.wav          -resample pc 22050
effects\eng_cloudCar_hi_lp.wav           -resample pc 22050
#endifplatform pc


// Common to Xwing Ywing Jedifighter Naboostarfighter -------------------------------------------------------------
#ifplatform pc
..\..\global\effects\droid_r2_chatter_01.wav -resample pc 22050
..\..\global\effects\droid_r2_chatter_02.wav -resample pc 22050
..\..\global\effects\Ifc_LowShield03.wav     -resample pc 22050
..\..\global\effects\Ifc_LowHealth02.wav     -resample pc 22050
//..\..\global\effects\droid_r2_chatter_03.wav -resample pc 22050
//..\..\global\effects\droid_r2_chatter_04.wav -resample pc 22050
..\..\global\effects\droid_r2_damage.wav     -resample pc 22050
..\..\global\effects\droid_r2_death.wav      -resample pc 22050
#endifplatform pc

// TIE -----------------------------------------------------------------------------------------------------------
// ----- TIE Common -----
#ifplatform pc
..\..\gcw\effects\wpn_tie_blaster_long.wav         -resample pc 44100
..\..\gcw\effects\eng_tieFighter_hi_lp.wav         -resample pc 22050
..\..\gcw\effects\eng_tieBomber_mid_lp.wav         -resample pc 22050
..\..\gcw\effects\eng_tieFighter_mid_lp.wav        -resample pc 22050
#endifplatform pc


// ----- TIE Bomber -----
#ifplatform pc
..\..\gcw\effects\wpn_tie_bombLauncher_fire.wav    -resample pc 44100
#endifplatform pc

// ---------------------------------------------------------------------------------------------------------------

// Xwing ----------------------------------------------------------------------------------------------
#ifplatform pc
..\..\gcw\effects\wpn_xwing_blaster_fire.wav    -resample pc 44100
//..\..\gcw\effects\wpn_xwing_torpedo_fire.wav    -resample pc 44100
..\..\gcw\effects\eng_xwing_hi_lp.wav           -resample pc 22050
..\..\gcw\effects\eng_xwing_low_lp.wav          -resample pc 22050
..\..\gcw\effects\eng_xwing_med_lp.wav          -resample pc 22050
#endifplatform pc

// ---------------------------------------------------------------------------------------------------------------


// Ywing ----------------------------------------------------------------------------------------------
#ifplatform pc
..\..\gcw\effects\wpn_ywing_blaster_fire.wav     -resample pc 44100
//..\..\gcw\effects\wpn_ywing_ionCannon_fire.wav   -resample pc 22050
..\..\gcw\effects\wpn_ywing_torpedo_fire.wav     -resample pc 44100
..\..\gcw\effects\eng_ywing_hi_lp.wav            -resample pc 22050
..\..\gcw\effects\eng_ywing_low_lp.wav           -resample pc 22050
..\..\gcw\effects\eng_ywing_mid_lp.wav           -resample pc 22050
#endifplatform pc

// ---------------------------------------------------------------------------------------------------------------

// Metal Debris -------------------------------------------------------------------------------------------------
#ifplatform pc
..\..\global\effects\exp_debris_metal_large01.wav  -resample pc 44100
..\..\global\effects\exp_debris_metal_med03.wav    -resample pc 44100
..\..\global\effects\exp_debris_metal_med02.wav    -resample pc 44100
..\..\global\effects\exp_debris_metal_small01.wav  -resample pc 44100
..\..\global\effects\exp_debris_metal_small03.wav  -resample pc 44100
#endifplatform pc

// --------------------------------------------------------------------------------------------------------------

// Ambient Emitters ---------------------------------------------------------------------------------------------
#ifplatform pc
..\YAV\effects\emt_telemetry_temple_lp01.wav            -resample pc 22050
..\YAV\effects\emt_telemetry_temple_lp02.wav            -resample pc 22050
#endifplatform pc
// --------------------------------------------------------------------------------------------------------------
```