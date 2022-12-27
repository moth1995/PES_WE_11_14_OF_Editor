import re
from tkinter import messagebox
from editor import common_functions, get_nation, get_nation_idx, get_nationality_by_demonyms, get_demonyms_by_nationality
class PSD():

    position_names = [
        [ "GK", "CWP", "CBT", "SB", "DM",  "WB", "CM",  "SM",  "AM",  "WG", "SS", "CF"],
        ["GK", "CWP", "CB",  "SB", "DMF", "WB", "CMF", "SMF", "AMF", "WF", "SS", "CF"],
    ]
    stat_names = [
        [ "Attack", "Defence", "Balance", "Stamina", "Speed", "Acceleration", "Response", "Agility", "Dribble Accuracy", "Dribble Speed", "Short Pass Accuracy", "Short Pass Speed", "Long Pass Accuracy", "Long Pass Speed", "Shot Accuracy", "Shot Power", "Shot Technique", "Free Kick Accuracy", "Swerve", "Heading", "Jump", "Technique", "Aggression", "Mentality", "GK Skills", "Team Work" ],

        [ "Attack", "Defence", "Balance", "Stamina", "Top Speed", "Acceleration", "Response", "Agility", "Dribble Accuracy", "Dribble Speed", "Short Pass Accuracy", "Short Pass Speed", "Long Pass Accuracy", "Long Pass Speed", "Shot Accuracy", "Shot Power", "Shot Technique", "Free Kick Accuracy", "Curling", "Header", "Jump", "Technique", "Aggression", "Mentality", "Keeper Skills", "Teamwork" ],

        [ "Attacking Prowess", "Defence Prowess", "Body Balance", "Stamina", "Speed", "Explosive Power", "Response", "Agility", "Dribbling", "Dribble Speed", "Low Pass", "Short Pass Speed", "Lofted Pass", "Long Pass Speed", "Finishing", "Kicking Power", "Shot Technique", "Place Kicking", "Controlled Spin", "Header", "Jump", "Ball Control", "Aggression", "Tenacity", "Goalkeeping", "Teamwork" ],

        [ "Attack", "Defence", "Balance", "Stamina", "Top Speed", "Explosive Power", "Reflexes", "Agility", "Dribble Accuracy", "Dribble Speed", "Short Pass Accuracy", "Short Pass Speed", "Long Pass Accuracy", "Long Pass Speed", "Shot Accuracy", "Kicking Power", "Shot Technique", "Place Kicking", "Curling", "Header Accuracy", "Jump", "Ball Controll", "Aggression", "Tenacity", "Goal Keeping Skills", "Teamwork" ]
    ]
    gui_ability_names = [
        [
            "Attack", "Defence", "Body Balance", "Stamina", "Top Speed", "Acceleration", "Response", "Agility", "Dribble Accuracy", "Dribble Speed", "Short Pass Accuracy", "Short Pass Speed", "Long Pass Accuracy", "Long Pass Speed", "Shot Accuracy", "Shot Power", "Shot Technique", "Free Kick Accuracy", "Swerve", "Heading", "Jump", "Technique", "Aggression", "Mentality", "Goal Keeping Skills", "Team Work Ability" ,
        ],
    ]
    ability_names = [
        "Dribbling", "Tactical dribble", "Positioning", "Reaction", "Playmaking", "Passing", "Scoring", "1-1 Scoring", "Post player", "Lines", "Middle shooting", "Side", "Centre", "Penalties", "1-Touch pass", "Outside", "Marking", "Sliding", "Covering", "D-Line control", "Penalty stopper", "1-On-1 stopper", "Long throw",
    ]

    gui_special_ability_names = [
        "Dribbling", "Tactical Dribble", "Positioning", "Reaction", "Playmaking", "Passing", "Scoring", "1-1 Scoring", "Post Player", "Lines", "Middle Shooting", "Side", "Centre", "Penalties", "1-Touch Pass", "Outside", "Marking", "Sliding Tackle", "Covering", "D-Line Control", "Penalty Stopper", "1-on-1 Stopper", "Long Throw",
    ]

    gui_position_names = [
        [
            "Goak Keeper (GK)", "Sweeper (CWP)", "Centre Back (CB)", "Side Back (SB)", "Defensive Midfielder (DMF)", "Wing Back (WB)", "Centre Midfielder (CMF)", "Side Midfielder (SMF)", "Attacking Midfielder (AMF)", "Wing Forward (WF)", "Second Striker (SS)", "Centre Forward (CF)",
        ],
    ]


    def psd_integer_parser(self, s:str):
        return common_functions.intTryParse(re.sub("[\\D]", "", s[1].strip().split(" ")[0]))

    def paste_psd(self, player_stats_window, clipboard, nations):

        lines = re.split("\\r?\\n", re.sub("(?m)^[ \t]*\r?\n", "",str(clipboard)))

        # First we set all special ability to zero
        for special_ability in player_stats_window.special_abilities_status_var:
            player_stats_window.special_abilities_status_var[special_ability].set(0)
        for position in player_stats_window.positions_status_var:
            player_stats_window.positions_status_var[position].set(0)

        for i in range(len(lines)):
            try:
                parts = lines[i].split(":")
                f = parts[0]
                if (len(parts)>1): #//ABILITY99!!
                    if f.lower() in "name".lower():
                        psd_name = parts[1].strip()
                        #print("Found name >", psd_name)
                        player_stats_window.player_name_entry.delete(0,"end")
                        player_stats_window.player_name_entry.insert(0,psd_name)
                        continue
                    if "Shirt Name".lower() in f.lower():
                        psd_shirt_name = parts[1].strip()
                        #print("Found shirt name >", psd_shirt_name)
                        player_stats_window.player_shirt_name_entry.delete(0,"end")
                        player_stats_window.player_shirt_name_entry.insert(0,psd_shirt_name)
                        continue

                    if ((f.lower() in "Callname".lower())):
                        callname = self.psd_integer_parser(parts)
                        #print(f"Found callname >  > {callname}")
                        player_stats_window.player_callname_entry.delete(0, "end")
                        player_stats_window.player_callname_entry.insert(0, callname)
                        continue

                    if f.lower() in "Positions".lower():
                        #print("Found Positions! ", parts[1])
                        pos_list = parts[1].split(",")
                        for z in range(len(pos_list)):
                            tmp = pos_list[z].replace("★","").replace("*","").strip().upper()
                            tmp = re.sub("[^a-zA-Z0-9]", "", tmp);
                            get_out = False
                            for k in range(len(self.position_names)):
                                if get_out: break
                                for k1 in range(len(self.position_names[k])):
                                    # Others player position
                                    if tmp.upper() == self.position_names[k][k1].upper():
                                        get_out = True
                                        tmp = self.position_names[0][k1]
                                        #print(gui_position_names[0][k1])
                                        player_stats_window.positions_status_var[self.gui_position_names[0][k1]].set(1)
                            # registered position
                            if ("★".lower() in pos_list[z].lower()) or ("*".lower() in pos_list[z].lower()):
                                #print("Reg:"+tmp+" ")
                                
                                player_stats_window.positions_status_var[self.gui_position_names[0][self.position_names[0].index(tmp)]].set(1)
                                #print(gui_position_names[0][position_names[0].index(tmp)])
                                player_stats_window.player_registered_position_combobox.set(self.gui_position_names[0][self.position_names[0].index(tmp)])
                            #else:
                                #print(tmp+" ")
                        #print("")
                        continue

                    if (("Side".lower() in f.lower())):
                        side = parts[1].upper().strip()
                        #print(f"Found side > {side}")
                        player_stats_window.player_favored_side_combobox.set(side)
                        continue
                    if ((f.lower() in "Foot".lower())):
                        foot = parts[1].upper().strip()
                        #print(f"Found foot > > {foot}")
                        player_stats_window.player_stronger_foot_combobox.set(foot)
                        continue
                    if (f.lower() in "Nationality".lower()):
                        psd_nation = parts[1].strip().replace(" ","");
                        #print("Found Nationality >\"",psd_nation,"\"");
                        nation = get_nationality_by_demonyms(psd_nation)
                        #print(nation)
                        player_stats_window.player_nationality_combobox.set(get_nation(nations, get_nation_idx(nations, nation)))
                        continue
                    if ((f.lower() in "Age".lower())):

                        tmp = parts[1].replace("("," ").replace(" "," ")
                        #print("Age string>"+tmp+"<")
                        tmp = tmp.strip().split(" ")[0]
                        tmp = tmp.strip().replace(" ","")
                        #print("Age stringint>"+tmp)
                        age = common_functions.intTryParse(tmp)
                        #print(f"Found age >  > {age}")
                        player_stats_window.player_age_int_var.set(age)
                        continue
                    
                    if f.lower() in "Growth Type".lower():
                        psd_growth_type = parts[1].strip()
                        #print("Found psd_growth_type >", psd_growth_type)
                        player_stats_window.player_growth_type_combobox.set(psd_growth_type)
                        player_stats_window.player_growth_type_combobox.event_generate("<<ComboboxSelected>>")
                        continue

                    if f.lower() in "Face".lower() :
                        psd_face = parts[1].strip()
                        #print("Found Face >", psd_face)
                        player_stats_window.player_face_combobox.set(psd_face)
                        player_stats_window.player_face_combobox.event_generate("<<ComboboxSelected>>")
                        player_stats_window.toggle_appearance_menu(2)
                        continue

                    if ((f.lower() in "Skin".lower())):
                        psd_skin = self.psd_integer_parser(parts)
                        #print(f"Found Skin >  > {psd_skin}")
                        player_stats_window.player_skin_colour_combobox.set(psd_skin)
                        continue

                    if "Head Height".lower() in f.lower():
                        psd_h_height = parts[1].strip()
                        #print(f"Found Head Height >  > {psd_h_height}")
                        player_stats_window.player_head_height_int_var.set(psd_h_height)
                        continue

                    if "Head Width".lower() in f.lower():
                        psd_h_width = parts[1].strip()
                        #print(f"Found Head Width >  > {psd_h_width}")
                        player_stats_window.player_head_width_int_var.set(psd_h_width)
                        continue

                    if (("Face ID".lower() in f.lower())):
                        psd_face_idx = self.psd_integer_parser(parts)
                        #print(f"Found Face ID >  > {psd_face_idx}")
                        player_stats_window.player_face_idx_int_var.set(psd_face_idx)
                        continue

                    if ((f.lower() in "Hairstyle ID".lower())):
                        psd_hair = self.psd_integer_parser(parts)
                        #print(f"Found Hairstyle ID >  > {psd_hair}")
                        player_stats_window.player_hair_idx_int_var.set(psd_hair)
                        continue

                    if f.lower() in "Special Hairstyles 2".lower():
                        psd_spe_hair_2 = parts[1].strip()
                        #print("Found Special Hairstyles 2 >", psd_spe_hair_2)
                        player_stats_window.player_special_hairstyles_2_var.set(1 if psd_spe_hair_2 == "YES" else 0)
                        player_stats_window.toggle_appearance_menu(2)
                        continue

                    if ((f.lower() in "Height".lower())):
                        height = self.psd_integer_parser(parts)
                        #print(f"Found Height >  > {height}")
                        player_stats_window.player_height_entry.delete(0, "end")
                        player_stats_window.player_height_entry.insert(0, height)
                        continue
                    if ((f.lower() in "Weight".lower())):
                        weight = self.psd_integer_parser(parts)
                        #print(f"Found Weight {weight}")
                        player_stats_window.player_weight_entry.delete(0, "end")
                        player_stats_window.player_weight_entry.insert(0, weight)
                        continue
                    if (("Weak Foot Accuracy".lower() in f.lower())):
                        wfa = self.psd_integer_parser(parts)
                        #print("Found Weak Foot Accuracy > ",wfa)
                        #player_stats_window.abilities_1_8_entries["Weak Foot Accuracy"].delete(0,"end")
                        #player_stats_window.abilities_1_8_entries["Weak Foot Accuracy"].insert(0,wfa)
                        player_stats_window.abilities_1_8_entries["Weak Foot Accuracy"].set(wfa)
                        continue
                    if (("Weak Foot Frequency".lower() in f.lower() )):
                        wff = self.psd_integer_parser(parts)
                        #print("Found Weak Foot Frequency > ", wff)
                        #player_stats_window.abilities_1_8_entries["Weak Foot Frequency"].delete(0,"end")
                        #player_stats_window.abilities_1_8_entries["Weak Foot Frequency"].insert(0,wff)
                        player_stats_window.abilities_1_8_entries["Weak Foot Frequency"].set(wff)
                        continue
                    if (("Condition".lower() in f.lower()) or ("Fitness".lower() in f.lower())):
                        con = self.psd_integer_parser(parts)
                        #print("Found Condition > ",con)
                        #player_stats_window.abilities_1_8_entries["Condition/Fitness"].delete(0,"end")
                        #player_stats_window.abilities_1_8_entries["Condition/Fitness"].insert(0,con)
                        player_stats_window.abilities_1_8_entries["Condition/Fitness"].set(con)
                        continue
                    if ((f.lower() in "Consistency".lower())):
                        cons = self.psd_integer_parser(parts)
                        #print("Found Consistency > ",cons)
                        #player_stats_window.abilities_1_8_entries["Consistency"].delete(0,"end")
                        #player_stats_window.abilities_1_8_entries["Consistency"].insert(0,cons)
                        player_stats_window.abilities_1_8_entries["Consistency"].set(cons)
                        continue
                    if ("Injury".lower() in f.lower()):
                        inj = parts[1].upper().strip()[0:1]
                        #print("Found Injury Tolerance >",inj)
                        player_stats_window.player_injury_combobox.set(inj)
                        continue
                    if ((f.lower() in "Dribble Style".lower())):
                        ds = self.psd_integer_parser(parts)
                        #print("Found Dribble Style >",ds)
                        player_stats_window.player_style_of_dribble_combobox.set(ds)
                        continue
                    if ((f.lower() in "Free Kick Style".lower())):
                        fks = self.psd_integer_parser(parts)
                        #print("Found Dribble Style >",fks)
                        player_stats_window.player_free_kick_type_combobox.set(fks)
                        continue
                    if ((f.lower() in "Penalty Style".lower()) or (f.lower() in "Penalty Kick Style".lower())):
                        ps = self.psd_integer_parser(parts)
                        #print("Found Penalty Style >",ps)
                        player_stats_window.player_penalty_kick_combobox.set(ps)
                        continue
                    if (f.lower() in "Drop Kick Style".lower()):
                        dk = self.psd_integer_parser(parts)
                        #print("Found Drop Kick Style >",dk)
                        player_stats_window.player_drop_kick_style_combobox.set(dk)
                        continue
                    if "Physique type".lower() in f.lower():
                        psd_physique = parts[1].strip()
                        #print("Found psd_physique >", psd_physique)
                        player_stats_window.physique_type_cmb.set(psd_physique)
                        player_stats_window.physique_type_cmb.event_generate("<<ComboboxSelected>>")
                        continue
                    if (f.lower() in [key.lower()for key in (player_stats_window.body_parameters.keys())]):
                        body_param = self.psd_integer_parser(parts)
                        #print("Found Drop Kick Style >",dk)
                        player_stats_window.body_parameters[f.lower().title()].set(body_param)
                        continue

                    found_stat = False
                    stat_index = -1

                    for j in range(len(self.stat_names)):
                        if found_stat: break
                        for z in range(len(self.stat_names[j])):
                            if found_stat: break
                            if((self.stat_names[j][z].lower() in f.lower()) and (f.lower() in self.stat_names[j][z].lower())):
                                found_stat = True
                                stat_index = z

                    if (found_stat):
                        statt = self.psd_integer_parser(parts)
                        #print("Found stat: "+stat_names[0][stat_index],"=",f," value -> ", statt)
                        #player_stats_window.abilities_entries[gui_ability_names[0][stat_index]].delete(0, "end")
                        #player_stats_window.abilities_entries[gui_ability_names[0][stat_index]].insert(0, statt)
                        player_stats_window.abilities_entries[self.gui_ability_names[0][stat_index]].set(statt)
                    #else:
                        #print("Nope. "+f)
                else:
                    f = f.replace("★","").replace("*","").strip();
                    for z in range(len(self.ability_names)):
                        if ((self.ability_names[z].lower() in f.lower()) and (f.lower() in self.ability_names[z].lower())):
                            #print("Found special "+self.ability_names[z])
                            player_stats_window.special_abilities_status_var[self.gui_special_ability_names[z]].set(1)
                            break
                #print("")
            except Exception as e:
                messagebox.showerror(title = "PSD PASTE ERROR", message = e)


    def copy_psd(self, player_stats_window):
        abilities = ""
        for i, key in enumerate(player_stats_window.abilities_entries.keys()):
            abilities += "{}: {}\n".format(self.stat_names[1][i], player_stats_window.abilities_entries.get(key).get())
        
        special_abilities = "SPECIAL ABILITIES:\n"
        for i, key in enumerate(player_stats_window.special_abilities_status_var.keys()):
            if player_stats_window.special_abilities_status_var.get(key).get():
                special_abilities += "* {}\n".format(self.ability_names[i])
        positions = "Side: {}\nPositions: {}*".format(player_stats_window.player_favored_side_combobox.get(), self.position_names[1][player_stats_window.player_registered_position_combobox.current()])
        for i, key in enumerate(player_stats_window.positions_status_var.keys()):
            if player_stats_window.positions_status_var.get(key).get() and i !=player_stats_window.player_registered_position_combobox.current():
                positions += ", {}".format(self.position_names[1][i])

        physique = "Physique type: %s\n" % (player_stats_window.physique_type_cmb.get())
        for i, key in enumerate(player_stats_window.body_parameters.keys()):
            physique += "{}: {}\n".format(key, player_stats_window.body_parameters.get(key).get())

        
        
        psd_string = """Name: {}
Shirt Name: {}
Callname: {}
Nationality: {}
Age: {}
Foot: {}
{}
Injury Tolerance: {}
Growth Type: {}

APPEARANCE:
Face: {}
Skin: {}
Head Height: {}
Head Width: {}
Face ID: {}
Hairstyle ID: {}
Special Hairstyles 2: {}
Height: {} cm
Weight: {} kg

STATS:
{}Consistency: {}
Condition/Fitness: {}
Weak Foot Accuracy: {}
Weak Foot Frequency: {}

{}
MOTION STYLE:
Dribble Style: {}
Free Kick Style: {}
Penalty Style: {}
Drop Kick Style: {}
Goal Celebration 1: {}
Goal Celebration 2: {}

PHYSIQUE:
{}
""".format(
            *[
            player_stats_window.player_name_entry.get(),
            player_stats_window.player_shirt_name_entry.get(),
            common_functions.intTryParse(player_stats_window.player_callname_entry.get()),
            get_demonyms_by_nationality(player_stats_window.player_nationality_combobox.get()),
            common_functions.intTryParse(player_stats_window.player_age_int_var.get()),
            player_stats_window.player_stronger_foot_combobox.get(),
            positions,
            player_stats_window.player_injury_combobox.get(),
            player_stats_window.player_growth_type_combobox.get(),

            player_stats_window.player_face_combobox.get(),
            common_functions.intTryParse(player_stats_window.player_skin_colour_combobox.get()),
            common_functions.intTryParse(player_stats_window.player_head_height_int_var.get()),
            common_functions.intTryParse(player_stats_window.player_head_width_int_var.get()),
            common_functions.intTryParse(player_stats_window.player_face_idx_int_var.get()),
            common_functions.intTryParse(player_stats_window.player_hair_idx_int_var.get()),
            "YES" if player_stats_window.player_special_hairstyles_2_var.get() else "NO",
            common_functions.intTryParse(player_stats_window.player_height_entry.get()),
            common_functions.intTryParse(player_stats_window.player_weight_entry.get()),
            ], 
            abilities,
            *[
                common_functions.intTryParse(player_stats_window.abilities_1_8_entries.get(key).get()) for key in player_stats_window.abilities_1_8_entries.keys()
            ],
            special_abilities,
            common_functions.intTryParse(player_stats_window.player_style_of_dribble_combobox.get()),
            common_functions.intTryParse(player_stats_window.player_free_kick_type_combobox.get()),
            common_functions.intTryParse(player_stats_window.player_penalty_kick_combobox.get()),
            common_functions.intTryParse(player_stats_window.player_drop_kick_style_combobox.get()),
            player_stats_window.player_goal_celebration_1_combobox.get(),
            player_stats_window.player_goal_celebration_2_combobox.get(),
            physique,
        )
        return psd_string
    
    