import csv
from . import common_functions, Player, OptionFile
from .utils.constants import *

def load_csv(file:str, of:OptionFile):
    csvf = open(file, READ_MODE, encoding=UTF_8)
    # list to store the names of columns
    csv_reader = csv.reader(csvf, delimiter = COMMA_SEPARATOR)
    list_of_column_names = [] 
    
    # loop to iterate thorugh the rows of csv 
    for row in csv_reader: 
    
        # adding the first row 
        list_of_column_names = row
    
        # breaking the loop after the 
        # first iteration itself 
        break
    #print(list_of_column_names)
    if 'ID' in list_of_column_names:
        for row in csv_reader: 
            player_idx = common_functions.intTryParse(row[list_of_column_names.index('ID')])
            
            if player_idx<0: continue # if player id is negative or zero, then we go to the next row
            
            player = of.players[player_idx] if player_idx < Player.first_edited_id else of.edited_players[player_idx - Player.first_edited_id]
            player.init_stats()
            # Basic settings

            if 'NAME' in list_of_column_names:
                csv_name=(row[list_of_column_names.index('NAME')])
                player.name = csv_name
                
            if 'SHIRT_NAME' in list_of_column_names:
                csv_shirt_name=(row[list_of_column_names.index('SHIRT_NAME')])
                player.shirt_name = csv_shirt_name

            if 'CALLNAME ID' in list_of_column_names:
                csv_callName=common_functions.intTryParseStat(row[list_of_column_names.index('CALLNAME ID')], player.callname.name, player_idx)
                player.callname.set_value(csv_callName)
                
            if 'NATIONALITY' in list_of_column_names:
                csv_nation=row[list_of_column_names.index('NATIONALITY')]
                player.nation.set_value(csv_nation)
                
            if 'AGE' in list_of_column_names:
                csv_age=common_functions.intTryParseStat(row[list_of_column_names.index('AGE')], player.basic_settings.age.name, player_idx)
                player.basic_settings.age.set_value(csv_age)
                
            if 'STRONG FOOT' in list_of_column_names:
                csv_foot=row[list_of_column_names.index('STRONG FOOT')]
                player.basic_settings.stronger_foot.set_value(csv_foot)

            if 'INJURY TOLERANCE' in list_of_column_names:
                csv_injury=(row[list_of_column_names.index('INJURY TOLERANCE')])
                player.basic_settings.injury.set_value(csv_injury)
                
            if 'DRIBBLE STYLE' in list_of_column_names:
                csv_dribSty=common_functions.intTryParseStat(row[list_of_column_names.index('DRIBBLE STYLE')], player.basic_settings.style_of_dribble.name, player_idx)
                player.basic_settings.style_of_dribble.set_value(csv_dribSty)                

            if 'FREE KICK STYLE' in list_of_column_names:
                csv_freekick=common_functions.intTryParseStat(row[list_of_column_names.index('FREE KICK STYLE')], player.basic_settings.free_kick_type.name, player_idx)
                player.basic_settings.free_kick_type.set_value(csv_freekick)
                
            if 'PK STYLE' in list_of_column_names:
                csv_pkStyle=common_functions.intTryParseStat(row[list_of_column_names.index('PK STYLE')], player.basic_settings.penalty_kick.name, player_idx)
                player.basic_settings.penalty_kick.set_value(csv_pkStyle)
                
            if 'DROP KICK STYLE' in list_of_column_names:
                csv_dkSty=common_functions.intTryParseStat(row[list_of_column_names.index('DROP KICK STYLE')], player.basic_settings.drop_kick_style.name, player_idx)
                player.basic_settings.drop_kick_style.set_value(csv_dkSty)

            if 'GOAL CELEBRATION 1' in list_of_column_names:
                csv_goal_c1=common_functions.intTryParseStat(row[list_of_column_names.index('GOAL CELEBRATION 1')], player.basic_settings.goal_celebration_1.name, player_idx)
                player.basic_settings.goal_celebration_1.set_value(csv_goal_c1)

            if 'GOAL CELEBRATION 2' in list_of_column_names:
                csv_goal_c2=common_functions.intTryParseStat(row[list_of_column_names.index('GOAL CELEBRATION 2')], player.basic_settings.goal_celebration_2.name, player_idx)
                player.basic_settings.goal_celebration_2.set_value(csv_goal_c2)

                
            if 'GROWTH TYPE' in list_of_column_names:
                csv_growth_type=row[list_of_column_names.index('GROWTH TYPE')]
                player.basic_settings.growth_type.set_value(csv_growth_type)

            # Position settings


            if 'REGISTERED POSITION' in list_of_column_names:
                csv_regPos=common_functions.intTryParseStat(row[list_of_column_names.index('REGISTERED POSITION')], player.position.registered_position.name, player_idx)
                player.position.registered_position.set_value(csv_regPos)
            
            if 'FAVOURED SIDE' in list_of_column_names:
                csv_favSide=(row[list_of_column_names.index('FAVOURED SIDE')])
                player.position.favored_side.set_value(csv_favSide)                   

            if 'GK  0' in list_of_column_names:
                csv_gk=common_functions.intTryParseStat(row[list_of_column_names.index('GK  0')], player.position.GK.name, player_idx)
                player.position.GK.set_value(csv_gk)
                
            if 'CWP  1' in list_of_column_names:
                csv_cbwS=common_functions.intTryParseStat(row[list_of_column_names.index('CWP  1')], player.position.CWP.name, player_idx)
                player.position.CWP.set_value(csv_cbwS)

            if 'CBT  2' in list_of_column_names:
                csv_cbt=common_functions.intTryParseStat(row[list_of_column_names.index('CBT  2')], player.position.CB.name, player_idx)
                player.position.CB.set_value(csv_cbt)

            if 'SB  3' in list_of_column_names:
                csv_sb=common_functions.intTryParseStat(row[list_of_column_names.index('SB  3')], player.position.SB.name, player_idx)
                player.position.SB.set_value(csv_sb)

            if 'DMF  4' in list_of_column_names:
                csv_dm=common_functions.intTryParseStat(row[list_of_column_names.index('DMF  4')], player.position.DM.name, player_idx)
                player.position.DM.set_value(csv_dm)

            if 'WB  5' in list_of_column_names:
                csv_wb=common_functions.intTryParseStat(row[list_of_column_names.index('WB  5')], player.position.WB.name, player_idx)
                player.position.WB.set_value(csv_wb)

            if 'CMF  6' in list_of_column_names:
                csv_cm=common_functions.intTryParseStat(row[list_of_column_names.index('CMF  6')], player.position.CM.name, player_idx)
                player.position.CM.set_value(csv_cm)
                
            if 'SMF  7' in list_of_column_names:
                csv_sm=common_functions.intTryParseStat(row[list_of_column_names.index('SMF  7')], player.position.SM.name, player_idx)
                player.position.SM.set_value(csv_sm)
                
            if 'AMF  8' in list_of_column_names:
                csv_om=common_functions.intTryParseStat(row[list_of_column_names.index('AMF  8')], player.position.AM.name, player_idx)
                player.position.AM.set_value(csv_om)
                
            if 'WF 9' in list_of_column_names:
                csv_wg=common_functions.intTryParseStat(row[list_of_column_names.index('WF 9')], player.position.WG.name, player_idx)
                player.position.WG.set_value(csv_wg)
                
            if 'SS  10' in list_of_column_names:
                csv_ss=common_functions.intTryParseStat(row[list_of_column_names.index('SS  10')], player.position.SS.name, player_idx)
                player.position.SS.set_value(csv_ss)
                
            if 'CF  11' in list_of_column_names:
                csv_cf=common_functions.intTryParseStat(row[list_of_column_names.index('CF  11')], player.position.CF.name, player_idx)
                player.position.CF.set_value(csv_cf)
                
            # Player ability settings     
                
                
            if 'WEAK FOOT ACCURACY' in list_of_column_names:
                csv_wfa=common_functions.intTryParseStat(row[list_of_column_names.index('WEAK FOOT ACCURACY')], player.abilities_1_8.weak_foot_accuracy.name, player_idx)
                player.abilities_1_8.weak_foot_accuracy.set_value(csv_wfa)
                
            if 'WEAK FOOT FREQUENCY' in list_of_column_names:
                csv_wff=common_functions.intTryParseStat(row[list_of_column_names.index('WEAK FOOT FREQUENCY')], player.abilities_1_8.weak_foot_frequency.name, player_idx)
                player.abilities_1_8.weak_foot_frequency.set_value(csv_wff)

            if 'ATTACK' in list_of_column_names:
                csv_attack=common_functions.intTryParseStat(row[list_of_column_names.index('ATTACK')], player.abilities.attack.name, player_idx)
                player.abilities.attack.set_value(csv_attack)
                
            if 'DEFENSE' in list_of_column_names:
                csv_defence=common_functions.intTryParseStat(row[list_of_column_names.index('DEFENSE')], player.abilities.defence.name, player_idx)
                player.abilities.defence.set_value(csv_defence)
                
            if 'BALANCE' in list_of_column_names:
                csv_balance=common_functions.intTryParseStat(row[list_of_column_names.index('BALANCE')], player.abilities.body_balance.name, player_idx)
                player.abilities.body_balance.set_value(csv_balance)
                
            if 'STAMINA' in list_of_column_names:
                csv_stamina=common_functions.intTryParseStat(row[list_of_column_names.index('STAMINA')], player.abilities.stamina.name, player_idx)
                player.abilities.stamina.set_value(csv_stamina)
                
            if 'TOP SPEED' in list_of_column_names:
                csv_speed=common_functions.intTryParseStat(row[list_of_column_names.index('TOP SPEED')], player.abilities.top_speed.name, player_idx)
                player.abilities.top_speed.set_value(csv_speed)
                
            if 'ACCELERATION' in list_of_column_names:
                csv_accel=common_functions.intTryParseStat(row[list_of_column_names.index('ACCELERATION')], player.abilities.acceleration.name, player_idx)
                player.abilities.acceleration.set_value(csv_accel)
                
            if 'RESPONSE' in list_of_column_names:
                csv_response=common_functions.intTryParseStat(row[list_of_column_names.index('RESPONSE')], player.abilities.response.name, player_idx)
                player.abilities.response.set_value(csv_response)
                
            if 'AGILITY' in list_of_column_names:
                csv_agility=common_functions.intTryParseStat(row[list_of_column_names.index('AGILITY')], player.abilities.agility.name, player_idx)
                player.abilities.agility.set_value(csv_agility)
                
            if 'DRIBBLE ACCURACY' in list_of_column_names:
                csv_dribAcc=common_functions.intTryParseStat(row[list_of_column_names.index('DRIBBLE ACCURACY')], player.abilities.dribble_accuracy.name, player_idx)
                player.abilities.dribble_accuracy.set_value(csv_dribAcc)
                
            if 'DRIBBLE SPEED' in list_of_column_names:
                csv_dribSpe=common_functions.intTryParseStat(row[list_of_column_names.index('DRIBBLE SPEED')], player.abilities.dribble_speed.name, player_idx)
                player.abilities.dribble_speed.set_value(csv_dribSpe)
                
            if 'SHORT PASS ACCURACY' in list_of_column_names:
                csv_sPassAcc=common_functions.intTryParseStat(row[list_of_column_names.index('SHORT PASS ACCURACY')], player.abilities.short_pass_accuracy.name, player_idx)
                player.abilities.short_pass_accuracy.set_value(csv_sPassAcc)
                
            if 'SHORT PASS SPEED' in list_of_column_names:
                csv_sPassSpe=common_functions.intTryParseStat(row[list_of_column_names.index('SHORT PASS SPEED')], player.abilities.short_pass_speed.name, player_idx)
                player.abilities.short_pass_speed.set_value(csv_sPassSpe)
                
            if 'LONG PASS ACCURACY' in list_of_column_names:
                csv_lPassAcc=common_functions.intTryParseStat(row[list_of_column_names.index('LONG PASS ACCURACY')], player.abilities.long_pass_accuracy.name, player_idx)
                player.abilities.long_pass_accuracy.set_value(csv_lPassAcc)
                
            if 'LONG PASS SPEED' in list_of_column_names:
                csv_lPassSpe=common_functions.intTryParseStat(row[list_of_column_names.index('LONG PASS SPEED')], player.abilities.long_pass_speed.name, player_idx)
                player.abilities.long_pass_speed.set_value(csv_lPassSpe)
                
            if 'SHOT ACCURACY' in list_of_column_names:
                csv_shotAcc=common_functions.intTryParseStat(row[list_of_column_names.index('SHOT ACCURACY')], player.abilities.shot_accuracy.name, player_idx)
                player.abilities.shot_accuracy.set_value(csv_shotAcc)
                
            if 'SHOT POWER' in list_of_column_names:
                csv_shotPow=common_functions.intTryParseStat(row[list_of_column_names.index('SHOT POWER')], player.abilities.shot_power.name, player_idx)
                player.abilities.shot_power.set_value(csv_shotPow)
                
            if 'SHOT TECHNIQUE' in list_of_column_names:
                csv_shotTec=common_functions.intTryParseStat(row[list_of_column_names.index('SHOT TECHNIQUE')], player.abilities.shot_technique.name, player_idx)
                player.abilities.shot_technique.set_value(csv_shotTec)
                
            if 'FREE KICK ACCURACY' in list_of_column_names:
                csv_fk=common_functions.intTryParseStat(row[list_of_column_names.index('FREE KICK ACCURACY')], player.abilities.free_kick_accuracy.name, player_idx)
                player.abilities.free_kick_accuracy.set_value(csv_fk)
                
            if 'SWERVE' in list_of_column_names:
                csv_swerve=common_functions.intTryParseStat(row[list_of_column_names.index('SWERVE')], player.abilities.swerve.name, player_idx)
                player.abilities.swerve.set_value(csv_swerve)
                
            if 'HEADING' in list_of_column_names:
                csv_heading=common_functions.intTryParseStat(row[list_of_column_names.index('HEADING')], player.abilities.heading.name, player_idx)
                player.abilities.heading.set_value(csv_heading)
                
            if 'JUMP' in list_of_column_names:
                csv_jump=common_functions.intTryParseStat(row[list_of_column_names.index('JUMP')], player.abilities.jump.name, player_idx)
                player.abilities.jump.set_value(csv_jump)
                
            if 'TECHNIQUE' in list_of_column_names:
                csv_tech=common_functions.intTryParseStat(row[list_of_column_names.index('TECHNIQUE')], player.abilities.technique.name, player_idx)
                player.abilities.technique.set_value(csv_tech)
                
            if 'AGGRESSION' in list_of_column_names:
                csv_aggress=common_functions.intTryParseStat(row[list_of_column_names.index('AGGRESSION')], player.abilities.aggression.name, player_idx)
                player.abilities.aggression.set_value(csv_aggress)
                
            if 'MENTALITY' in list_of_column_names:
                csv_mental=common_functions.intTryParseStat(row[list_of_column_names.index('MENTALITY')], player.abilities.mentality.name, player_idx)
                player.abilities.mentality.set_value(csv_mental)
                
            if 'CONSISTENCY' in list_of_column_names:
                csv_consistency=common_functions.intTryParseStat(row[list_of_column_names.index('CONSISTENCY')], player.abilities_1_8.consistency.name, player_idx)
                player.abilities_1_8.consistency.set_value(csv_consistency)
                
            if 'GOAL KEEPING' in list_of_column_names:
                csv_gkAbil=common_functions.intTryParseStat(row[list_of_column_names.index('GOAL KEEPING')], player.abilities.goal_keeping_skills.name, player_idx)
                player.abilities.goal_keeping_skills.set_value(csv_gkAbil)
                
            if 'TEAM WORK' in list_of_column_names:
                csv_team=common_functions.intTryParseStat(row[list_of_column_names.index('TEAM WORK')], player.abilities.team_work_ability.name, player_idx)
                player.abilities.team_work_ability.set_value(csv_team)
                
            if 'CONDITION / FITNESS' in list_of_column_names:
                csv_condition=common_functions.intTryParseStat(row[list_of_column_names.index('CONDITION / FITNESS')], player.abilities_1_8.condition_fitness.name, player_idx)
                player.abilities_1_8.condition_fitness.set_value(csv_condition)
                
            if 'DRIBBLING' in list_of_column_names:
                csv_drib=common_functions.intTryParseStat(row[list_of_column_names.index('DRIBBLING')], player.special_abilities.dribbling.name, player_idx)
                player.special_abilities.dribbling.set_value(csv_drib)
                
            if 'TACTICAL DRIBBLE' in list_of_column_names:
                csv_dribKeep=common_functions.intTryParseStat(row[list_of_column_names.index('TACTICAL DRIBBLE')], player.special_abilities.tactical_dribble.name, player_idx)
                player.special_abilities.tactical_dribble.set_value(csv_dribKeep)
                
            if 'POST PLAYER' in list_of_column_names:
                csv_post=common_functions.intTryParseStat(row[list_of_column_names.index('POST PLAYER')], player.special_abilities.post_player.name, player_idx)
                player.special_abilities.post_player.set_value(csv_post)
                
            if 'POSITIONING' in list_of_column_names:
                csv_posit=common_functions.intTryParseStat(row[list_of_column_names.index('POSITIONING')], player.special_abilities.positioning.name, player_idx)
                player.special_abilities.positioning.set_value(csv_posit)
                
            if 'REACTION' in list_of_column_names:
                csv_offside=common_functions.intTryParseStat(row[list_of_column_names.index('REACTION')], player.special_abilities.reaction.name, player_idx)
                player.special_abilities.reaction.set_value(csv_offside)

            if 'LINES' in list_of_column_names:
                csv_linePos=common_functions.intTryParseStat(row[list_of_column_names.index('LINES')], player.special_abilities.lines.name, player_idx)
                player.special_abilities.lines.set_value(csv_linePos)

            if 'MIDDLE SHOOTING' in list_of_column_names:
                csv_midShot=common_functions.intTryParseStat(row[list_of_column_names.index('MIDDLE SHOOTING')], player.special_abilities.middle_shooting.name, player_idx)
                player.special_abilities.middle_shooting.set_value(csv_midShot)

            if 'SCORING' in list_of_column_names:
                csv_scorer=common_functions.intTryParseStat(row[list_of_column_names.index('SCORING')], player.special_abilities.scoring.name, player_idx)
                player.special_abilities.scoring.set_value(csv_scorer)

            if 'PLAYMAKING' in list_of_column_names:
                csv_play=common_functions.intTryParseStat(row[list_of_column_names.index('PLAYMAKING')], player.special_abilities.playmaking.name, player_idx)
                player.special_abilities.playmaking.set_value(csv_play)

            if 'PASSING' in list_of_column_names:
                csv_pass=common_functions.intTryParseStat(row[list_of_column_names.index('PASSING')], player.special_abilities.passing.name, player_idx)
                player.special_abilities.passing.set_value(csv_pass)

            if 'PENALTIES' in list_of_column_names:
                csv_pk=common_functions.intTryParseStat(row[list_of_column_names.index('PENALTIES')], player.special_abilities.penalties.name, player_idx)
                player.special_abilities.penalties.set_value(csv_pk)

            if '1-1 SCORING' in list_of_column_names:
                csv_k11=common_functions.intTryParseStat(row[list_of_column_names.index('1-1 SCORING')], player.special_abilities.one_on_one_scoring.name, player_idx)
                player.special_abilities.one_on_one_scoring.set_value(csv_k11)

            if 'LONG THROW' in list_of_column_names:
                csv_longThrow=common_functions.intTryParseStat(row[list_of_column_names.index('LONG THROW')], player.special_abilities.long_throw.name, player_idx)
                player.special_abilities.long_throw.set_value(csv_longThrow)

            if '1-TOUCH PASS' in list_of_column_names:
                csv_direct=common_functions.intTryParseStat(row[list_of_column_names.index('1-TOUCH PASS')], player.special_abilities.one_touch_pass.name, player_idx)
                player.special_abilities.one_touch_pass.set_value(csv_direct)

            if 'SIDE' in list_of_column_names:
                csv_side=common_functions.intTryParseStat(row[list_of_column_names.index('SIDE')], player.special_abilities.side.name, player_idx)
                player.special_abilities.side.set_value(csv_side)

            if 'CENTRE' in list_of_column_names:
                csv_centre=common_functions.intTryParseStat(row[list_of_column_names.index('CENTRE')], player.special_abilities.centre.name, player_idx)
                player.special_abilities.centre.set_value(csv_centre)

            if 'OUTSIDE' in list_of_column_names:
                csv_outside=common_functions.intTryParseStat(row[list_of_column_names.index('OUTSIDE')], player.special_abilities.outside.name, player_idx)
                player.special_abilities.outside.set_value(csv_outside)

            if 'MARKING' in list_of_column_names:
                csv_man=common_functions.intTryParseStat(row[list_of_column_names.index('MARKING')], player.special_abilities.marking.name, player_idx)
                player.special_abilities.marking.set_value(csv_man)

            if 'D-LINE CONTROL' in list_of_column_names:
                csv_dLine=common_functions.intTryParseStat(row[list_of_column_names.index('D-LINE CONTROL')], player.special_abilities.d_line_control.name, player_idx)
                player.special_abilities.d_line_control.set_value(csv_dLine)

            if 'SLIDING' in list_of_column_names:
                csv_slide=common_functions.intTryParseStat(row[list_of_column_names.index('SLIDING')], player.special_abilities.sliding_tackle.name, player_idx)
                player.special_abilities.sliding_tackle.set_value(csv_slide)

            if 'COVERING' in list_of_column_names:
                csv_cover=common_functions.intTryParseStat(row[list_of_column_names.index('COVERING')], player.special_abilities.covering.name, player_idx)
                player.special_abilities.covering.set_value(csv_cover)

            if 'PENALTY STOPPER' in list_of_column_names:
                csv_keeperPK=common_functions.intTryParseStat(row[list_of_column_names.index('PENALTY STOPPER')], player.special_abilities.penalty_stopper.name, player_idx)
                player.special_abilities.penalty_stopper.set_value(csv_keeperPK)

            if '1-ON-1 STOPPER' in list_of_column_names:
                csv_keeper11=common_functions.intTryParseStat(row[list_of_column_names.index('1-ON-1 STOPPER')], player.special_abilities.one_on_one_stopper.name, player_idx)
                player.special_abilities.one_on_one_stopper.set_value(csv_keeper11)

            if 'FACE TYPE' in list_of_column_names:
                csv_face_type = (row[list_of_column_names.index('FACE TYPE')])
                player.appearance.face.set_value(csv_face_type)

            if 'SKIN COLOUR' in list_of_column_names:
                csv_skin_colour = common_functions.intTryParseStat(row[list_of_column_names.index('SKIN COLOUR')], player.appearance.skin_colour.name, player_idx)
                player.appearance.skin_colour.set_value(csv_skin_colour)

            if 'HEAD HEIGHT' in list_of_column_names:
                csv_head_height = common_functions.intTryParseStat(row[list_of_column_names.index('HEAD HEIGHT')], player.appearance.head_height.name, player_idx)
                player.appearance.head_height.set_value(csv_head_height)

            if 'HEAD WIDTH' in list_of_column_names:
                csv_head_width = common_functions.intTryParseStat(row[list_of_column_names.index('HEAD WIDTH')], player.appearance.head_width.name, player_idx)
                player.appearance.head_width.set_value(csv_head_width)

            if 'FACE ID' in list_of_column_names:
                csv_face_id = common_functions.intTryParseStat(row[list_of_column_names.index('FACE ID')], player.appearance.face_idx.name, player_idx)
                player.appearance.face_idx.set_value(csv_face_id)

            """
            if 'HEAD OVERALL POSITION' in list_of_column_names:
                csv_head_ov_pos = common_functions.intTryParseStat(row[list_of_column_names.index('HEAD OVERALL POSITION')])
                

            # Brows menu
            if 'BROWS TYPE' in list_of_column_names:
                csv_brows_type = common_functions.intTryParseStat(row[list_of_column_names.index('BROWS TYPE')])

            if 'BROWS ANGLE' in list_of_column_names:
                csv_brows_angle = common_functions.intTryParseStat(row[list_of_column_names.index('BROWS ANGLE')])

            if 'BROWS HEIGHT' in list_of_column_names:
                csv_brows_height = common_functions.intTryParseStat(row[list_of_column_names.index('BROWS HEIGHT')])

            if 'BROWS SPACING' in list_of_column_names:
                csv_brows_spacing = common_functions.intTryParseStat(row[list_of_column_names.index('BROWS SPACING')])

            # Eyes menu
            if 'EYES TYPE' in list_of_column_names:
                csv_eyes_type = common_functions.intTryParseStat(row[list_of_column_names.index('EYES TYPE')])

            if 'EYES POSITION' in list_of_column_names:
                csv_eyes_position = common_functions.intTryParseStat(row[list_of_column_names.index('EYES POSITION')])

            if 'EYES ANGLE' in list_of_column_names:
                csv_eyes_angle = common_functions.intTryParseStat(row[list_of_column_names.index('EYES ANGLE')])

            if 'EYES LENGTH' in list_of_column_names:
                csv_eyes_lenght = common_functions.intTryParseStat(row[list_of_column_names.index('EYES LENGTH')])

            if 'EYES WIDTH' in list_of_column_names:
                csv_eyes_width = common_functions.intTryParseStat(row[list_of_column_names.index('EYES WIDTH')])

            if 'EYES COLOUR 1' in list_of_column_names:
                csv_eyes_c1 = common_functions.intTryParseStat(row[list_of_column_names.index('EYES COLOUR 1')])

            if 'EYES COLOUR 2' in list_of_column_names:
                csv_eyes_c2 = (row[list_of_column_names.index('EYES COLOUR 2')])


            # Nose menu
            if 'NOSE TYPE' in list_of_column_names:
                csv_nose_type = common_functions.intTryParseStat(row[list_of_column_names.index('NOSE TYPE')])

            if 'NOSE HEIGHT' in list_of_column_names:
                csv_nose_height = common_functions.intTryParseStat(row[list_of_column_names.index('NOSE HEIGHT')])

            if 'NOSE WIDTH' in list_of_column_names:
                csv_nose_width = common_functions.intTryParseStat(row[list_of_column_names.index('NOSE WIDTH')])

            # Cheecks menu
            if 'CHEECKS TYPE' in list_of_column_names:
                csv_cheecks_type = common_functions.intTryParseStat(row[list_of_column_names.index('CHEECKS TYPE')])

            if 'CHEECKS SHAPE' in list_of_column_names:
                csv_cheecks_shape = common_functions.intTryParseStat(row[list_of_column_names.index('CHEECKS SHAPE')])

            # Mouth menu
            if 'MOUTH TYPE' in list_of_column_names:
                csv_mouth_type = common_functions.intTryParseStat(row[list_of_column_names.index('MOUTH TYPE')])

            if 'MOUTH SIZE' in list_of_column_names:
                csv_mouth_size = common_functions.intTryParseStat(row[list_of_column_names.index('MOUTH SIZE')])

            if 'MOUTH POSITION' in list_of_column_names:
                csv_mouth_position = common_functions.intTryParseStat(row[list_of_column_names.index('MOUTH POSITION')])

            # Jaw menu
            if 'JAW TYPE' in list_of_column_names:
                csv_jaw_type = common_functions.intTryParseStat(row[list_of_column_names.index('JAW TYPE')])

            if 'JAW CHIN' in list_of_column_names:
                csv_jaw_chin = common_functions.intTryParseStat(row[list_of_column_names.index('JAW CHIN')])

            if 'JAW WIDTH' in list_of_column_names:
                csv_jaw_width = common_functions.intTryParseStat(row[list_of_column_names.index('JAW WIDTH')])
            """
            # Hair
            if 'HAIR ID' in list_of_column_names:
                csv_hair = common_functions.intTryParseStat(row[list_of_column_names.index('HAIR ID')], player.appearance.hair.name, player_idx)
                player.appearance.hair.set_value(csv_hair)

            if 'IS SPECIAL HAIRSTYLE 2' in list_of_column_names:
                csv_hair = row[list_of_column_names.index('IS SPECIAL HAIRSTYLE 2')]
                player.appearance.special_hairstyles_2.set_value(csv_hair)
            """
            # If we dont find any of those columns in our csv file we dont import the hair attributes
            if (("HAIR TYPE" in list_of_column_names) and ("HAIR SHAPE" in list_of_column_names) and ("HAIR FRONT" in list_of_column_names) and ("HAIR VOLUME" in list_of_column_names) and ("HAIR DARKNESS" in list_of_column_names) and ("BANDANA" in list_of_column_names)):
                csv_hair = 0
                csv_hair_type = row[list_of_column_names.index('HAIR TYPE')]
                csv_hair_shape = int(row[list_of_column_names.index('HAIR SHAPE')])
                csv_hair_front = int(row[list_of_column_names.index('HAIR FRONT')])
                csv_hair_volume = int(row[list_of_column_names.index('HAIR VOLUME')])
                csv_hair_darkness = int(row[list_of_column_names.index('HAIR DARKNESS')])
                csv_hair_bandana = int(row[list_of_column_names.index('BANDANA')])

                if csv_hair_type == 'BALD':
                    csv_hair = csv_hair_shape

                elif csv_hair_type == 'BUZZ CUT':
                    csv_hair = 4 + (csv_hair_darkness) + (csv_hair_front * 4) + (csv_hair_shape * 20)

                elif csv_hair_type == 'VERY SHORT 1':
                    csv_hair = 84 + (csv_hair_front) + (csv_hair_shape * 6)

                elif csv_hair_type == 'VERY SHORT 2':
                    if 0 <= csv_hair_shape <= 2:
                        csv_hair = 108 + (csv_hair_shape * 10) + (csv_hair_front)
                    else:
                        csv_hair = 138 + ((csv_hair_shape - 3) * 5) + (csv_hair_front)

                elif csv_hair_type == 'STRAIGHT 1':
                    if 0 <= csv_hair_front <= 8:
                        csv_hair = 153 + csv_hair_bandana + csv_hair_volume * 3 + csv_hair_front * 9 + csv_hair_shape * 102
                    else:
                        csv_hair = 234 + csv_hair_volume + (csv_hair_front - 9) * 3 + csv_hair_shape * 102

                elif csv_hair_type == 'STRAIGHT 2':
                    if 0 <= csv_hair_front <= 1:
                        csv_hair = 561 + csv_hair_bandana + csv_hair_volume * 3 + csv_hair_front * 9 + csv_hair_shape * 33
                    else:
                        csv_hair = 579 + csv_hair_volume + (csv_hair_front - 2) * 3 + csv_hair_shape * 33
                        
                elif csv_hair_type == 'CURLY 1':
                    if 0 <= csv_hair_front <= 4:
                        csv_hair = 660 + csv_hair_bandana + csv_hair_volume * 3 + csv_hair_front * 9 + csv_hair_shape * 51
                    else:
                        csv_hair = 705 + csv_hair_volume + (csv_hair_front - 5) * 3 + csv_hair_shape * 51

                elif csv_hair_type == 'CURLY 2':
                    csv_hair = 864 + csv_hair_volume + csv_hair_front * 2 + csv_hair_shape * 12

                elif csv_hair_type == 'PONYTAIL 1':
                    csv_hair = 912 + csv_hair_volume + csv_hair_front * 3 + csv_hair_shape * 12

                elif csv_hair_type == 'PONYTAIL 2':
                    csv_hair = 948 + csv_hair_volume + csv_hair_front * 3 + csv_hair_shape * 12

                elif csv_hair_type == 'DREADLOCKS':
                    csv_hair = 984 + csv_hair_volume + csv_hair_front * 2 + csv_hair_shape * 8

                elif csv_hair_type == 'PULLED BACK':
                    csv_hair = 1008 + csv_hair_front + csv_hair_shape * 6

                elif csv_hair_type == 'SPECIAL HAIRSTYLES':
                    csv_hair = 1026 + csv_hair_shape

                set_value(of, player_id, 45, 0, 2047, csv_hair)
            """
            """
            if 'HAIR COLOUR CONFIG' in list_of_column_names:
                csv_hair_colour_config = common_functions.intTryParseStat(row[list_of_column_names.index('HAIR COLOUR CONFIG')])

            if 'HAIR COLOUR RGB R' in list_of_column_names:
                csv_hair_rgb_r = common_functions.intTryParseStat(row[list_of_column_names.index('HAIR COLOUR RGB R')]) 

            if 'HAIR COLOUR RGB G' in list_of_column_names:
                csv_hair_rgb_g = common_functions.intTryParseStat(row[list_of_column_names.index('HAIR COLOUR RGB G')])

            if 'HAIR COLOUR RGB B' in list_of_column_names:
                csv_hair_rgb_b = common_functions.intTryParseStat(row[list_of_column_names.index('HAIR COLOUR RGB B')])

            if 'BANDANA COLOUR' in list_of_column_names:
                csv_hair_bandana_colour = common_functions.intTryParseStat(row[list_of_column_names.index('BANDANA COLOUR')])

            if 'CAP (ONLY GK)' in list_of_column_names:
                csv_cap = common_functions.intTryParseStat(row[list_of_column_names.index('CAP (ONLY GK)')])

            if 'CAP COLOUR' in list_of_column_names:
                csv_cap_colour = common_functions.intTryParseStat(row[list_of_column_names.index('CAP COLOUR')])

            if 'FACIAL HAIR TYPE' in list_of_column_names:
                csv_facial_hair_type = common_functions.intTryParseStat(row[list_of_column_names.index('FACIAL HAIR TYPE')])

            if 'FACIAL HAIR COLOUR' in list_of_column_names:
                csv_facial_hair_colour = common_functions.intTryParseStat(row[list_of_column_names.index('FACIAL HAIR COLOUR')])

            if 'SUNGLASSES TYPE' in list_of_column_names:
                csv_sunglasses = common_functions.intTryParseStat(row[list_of_column_names.index('SUNGLASSES TYPE')]) 

            if 'SUNGLASSES COLOUR' in list_of_column_names:
                csv_sunglasses_colour = common_functions.intTryParseStat(row[list_of_column_names.index('SUNGLASSES COLOUR')])
            """
            # Physical settings
            if 'HEIGHT' in list_of_column_names:
                csv_height=common_functions.intTryParseStat(row[list_of_column_names.index('HEIGHT')], player.appearance.height.name, player_idx)
                player.appearance.height.set_value(csv_height)

            if 'WEIGHT' in list_of_column_names:
                csv_weight=common_functions.intTryParseStat(row[list_of_column_names.index('WEIGHT')], player.appearance.weight.name, player_idx)
                player.appearance.weight.set_value(csv_weight)

            if 'BODY TYPE' in list_of_column_names:
                csv_body_type=(row[list_of_column_names.index('BODY TYPE')])
                if csv_body_type == "Edit":
                    if 'NECK LENGTH' in list_of_column_names:
                        csv_neck_length = common_functions.intTryParseStat(row[list_of_column_names.index('NECK LENGTH')], player.appearance.neck_length.name, player_idx)
                        player.appearance.leg_length.set_value(csv_neck_length)

                    if 'NECK WIDTH' in list_of_column_names:
                        csv_neck_width = common_functions.intTryParseStat(row[list_of_column_names.index('NECK WIDTH')], player.appearance.neck_width.name, player_idx)
                        player.appearance.neck_width.set_value(csv_neck_width)
                        
                    if 'SHOULDER HEIGHT' in list_of_column_names:
                        csv_shoulder_height = common_functions.intTryParseStat(row[list_of_column_names.index('SHOULDER HEIGHT')], player.appearance.shoulder_height.name, player_idx)
                        player.appearance.shoulder_height.set_value(csv_shoulder_height)
                        
                    if 'SHOULDER WIDTH' in list_of_column_names:
                        csv_should_width = common_functions.intTryParseStat(row[list_of_column_names.index('SHOULDER WIDTH')], player.appearance.shoulder_width.name, player_idx)
                        player.appearance.shoulder_width.set_value(csv_should_width)

                    if 'CHEST MEASUREMENT' in list_of_column_names:
                        csv_chest_measu = common_functions.intTryParseStat(row[list_of_column_names.index('CHEST MEASUREMENT')], player.appearance.chest_measu.name, player_idx)
                        player.appearance.chest_measu.set_value(csv_chest_measu)

                    if 'WAIST CIRCUMFERENCE' in list_of_column_names:
                        csv_waist_circu = common_functions.intTryParseStat(row[list_of_column_names.index('WAIST CIRCUMFERENCE')], player.appearance.waist_circumference.name, player_idx)
                        player.appearance.waist_circumference.set_value(csv_waist_circu)

                    if 'ARM CIRCUMFERENCE' in list_of_column_names:
                        csv_arm_circu = common_functions.intTryParseStat(row[list_of_column_names.index('ARM CIRCUMFERENCE')], player.appearance.arm_circumference.name, player_idx)
                        player.appearance.arm_circumference.set_value(csv_arm_circu)

                    if 'LEG CIRCUMFERENCE' in list_of_column_names:
                        csv_leg_circu = common_functions.intTryParseStat(row[list_of_column_names.index('LEG CIRCUMFERENCE')], player.appearance.leg_circumference.name, player_idx)
                        player.appearance.leg_circumference.set_value(csv_leg_circu)

                    if 'CALF CIRCUMFERENCE' in list_of_column_names:
                        csv_calf_circu = common_functions.intTryParseStat(row[list_of_column_names.index('CALF CIRCUMFERENCE')], player.appearance.calf_circumference.name, player_idx)
                        player.appearance.calf_circumference.set_value(csv_calf_circu)

                    if 'LEG LENGTH' in list_of_column_names:
                        csv_leg_length = common_functions.intTryParseStat(row[list_of_column_names.index('LEG LENGTH')], player.appearance.leg_length.name, player_idx)
                        player.appearance.leg_length.set_value(csv_leg_length)
                else:
                    csv_body_type=row[list_of_column_names.index('BODY TYPE')]
                    player.appearance.body_parameters = BODY_TYPES_VALUES[BODY_TYPES.index(csv_body_type)]
                    
                    
            """
            # Boots/Acc.
            if 'BOOT TYPE' in list_of_column_names:
                csv_boot_type = common_functions.intTryParseStat(row[list_of_column_names.index('BOOT TYPE')])

            if 'BOOT COLOUR' in list_of_column_names:
                csv_boot_colour = common_functions.intTryParseStat(row[list_of_column_names.index('BOOT COLOUR')])

            if 'NECK WARMER' in list_of_column_names:
                csv_neck_warm = common_functions.intTryParseStat(row[list_of_column_names.index('NECK WARMER')])

            if 'NECKLACE TYPE' in list_of_column_names:
                csv_necklace_type = common_functions.intTryParseStat(row[list_of_column_names.index('NECKLACE TYPE')])

            if 'NECKLACE COLOUR' in list_of_column_names:
                csv_necklace_colour = common_functions.intTryParseStat(row[list_of_column_names.index('NECKLACE COLOUR')])

            if 'WISTBAND' in list_of_column_names:
                csv_wistband = common_functions.intTryParseStat(row[list_of_column_names.index('WISTBAND')])

            if 'WISTBAND COLOUR' in list_of_column_names:
                csv_wistband_colour = common_functions.intTryParseStat(row[list_of_column_names.index('WISTBAND COLOUR')])

            if 'FRIENDSHIP BRACELET' in list_of_column_names:
                csv_friend_brace = common_functions.intTryParseStat(row[list_of_column_names.index('FRIENDSHIP BRACELET')])

            if 'FRIENDSHIP BRACELET COLOUR' in list_of_column_names:
                csv_friend_brace_colour = common_functions.intTryParseStat(row[list_of_column_names.index('FRIENDSHIP BRACELET COLOUR')])

            if 'GLOVES' in list_of_column_names:
                csv_gloves = int(row[list_of_column_names.index('GLOVES')])

            if 'FINGER BAND' in list_of_column_names:
                csv_finger_band = common_functions.intTryParseStat(row[list_of_column_names.index('FINGER BAND')])

            if 'SHIRT' in list_of_column_names:
                csv_shirt = common_functions.intTryParseStat(row[list_of_column_names.index('SHIRT')])

            if 'SLEEVES' in list_of_column_names:
                csv_sleeves = common_functions.intTryParseStat(row[list_of_column_names.index('SLEEVES')])

            if 'UNDER SHORT' in list_of_column_names:
                csv_under_short = common_functions.intTryParseStat(row[list_of_column_names.index('UNDER SHORT')])

            if 'UNDER SHORT COLOUR' in list_of_column_names:
                csv_under_short_colour = common_functions.intTryParseStat(row[list_of_column_names.index('UNDER SHORT COLOUR')])

            if 'SOCKS' in list_of_column_names:
                csv_socks = common_functions.intTryParseStat(row[list_of_column_names.index('SOCKS')])

            if 'TAPE' in list_of_column_names:
                csv_tape = common_functions.intTryParseStat(row[list_of_column_names.index('TAPE')])
            """
            # Here's a template in future case i need to add a new stat (which is very likely)
            #if '' in list_of_column_names:
                #csv_ = int(row[list_of_column_names.index('')])
                #print(player_id, csv_)
                #set_value(of, player_id, , , , csv_)

            # breaking the loop after the 
            # first iteration itself 
            #break
    else:
        raise ValueError("No ID Column was found on the CSV, data was not imported")
    csvf.close()

