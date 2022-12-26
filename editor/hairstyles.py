def normalize_hairstyle(hair:int):
    # Bald
    if 0 <= hair <= 3:
        hair_type = "BALD"
        hair_shape = hair + 1
        hair_front = 1
        hair_volume = 1
        hair_darkness = 1
        hair_bandana = 1
    # Buzz cut
    elif 4 <= hair <= 83:
        hair_type = "BUZZ CUT"
        hair_shape = 1
        hair_front = 1
        hair_volume = 1
        hair_darkness = 0
        hair_bandana = 1
        for c in range(4, hair + 1):
            hair_darkness += 1
            if hair_darkness == 5:
                hair_darkness = 1
                hair_front += 1
                if hair_front == 6:
                    hair_front = 1
                    hair_shape += 1
    # Very short 1
    elif 84 <= hair <= 107:
        hair_type = "VERY SHORT 1"
        hair_shape = 1
        hair_front = 0
        hair_volume = 1
        hair_darkness = 1
        hair_bandana = 1
        for c in range(84, hair +1 ):
            hair_front += 1
            if hair_front == 7:
                hair_front = 1
                hair_shape += 1
    # Very short 2
    elif 108 <= hair <= 152:
        hair_type = "VERY SHORT 2"
        hair_front = 0
        hair_volume = 1
        hair_darkness = 1
        hair_bandana = 1
        if hair >= 138:
            hair_shape = 4
            for c in range(138, hair + 1):
                hair_front += 1
                if hair_front == 6:
                    hair_front = 1
                    hair_shape += 1
        else:
            hair_shape = 1
            for c in range(108, hair + 1):
                hair_front += 1
                if hair_front == 11:
                    hair_front = 1
                    hair_shape += 1
    # Straight 1
    elif 153 <= hair <= 560:
        hair_type = "STRAIGHT 1"
        hair_shape = 1
        hair_front = 1
        hair_volume = 1
        hair_darkness = 1
        hair_bandana = 0
        for c in range(153, hair + 1):
            hair_bandana += 1
            if hair_bandana > 3 :
                hair_volume += 1
                hair_bandana = 1
                if hair_volume == 4 :
                    hair_front += 1
                    hair_volume = 1
                    if hair_front == 17 :
                        hair_shape += 1
                        hair_front = 1
                if hair_front >= 10:
                    hair_bandana = 4
    # Straight 2
    elif 561 <= hair <= 659:
        hair_type = "STRAIGHT 2"
        hair_shape = 1
        hair_front = 1
        hair_volume = 1
        hair_darkness = 1
        hair_bandana = 0
        for c in range(561, hair + 1):
            hair_bandana += 1
            if hair_bandana > 3:
                hair_volume += 1
                hair_bandana = 1
                if hair_volume == 4:
                    hair_front += 1
                    hair_volume = 1
                    if hair_front == 8:
                        hair_shape += 1
                        hair_front = 1
                if hair_front >= 3:
                    hair_bandana = 4
    # Curly 1
    elif 660 <= hair <= 863:
        hair_type = "CURLY 1"
        hair_shape = 1
        hair_front = 1
        hair_volume = 1
        hair_darkness = 1
        hair_bandana = 0
        for c in range(660, hair + 1):
            hair_bandana += 1
            if hair_bandana > 3 :
                hair_volume += 1
                hair_bandana = 1
                if hair_volume == 4 :
                    hair_front += 1
                    hair_volume = 1
                    if hair_front == 8 :
                        hair_shape += 1
                        hair_front = 1
                if hair_front >= 6:
                    hair_bandana = 4
    # Curly 2
    elif 864 <= hair <= 911:
        hair_type = "CURLY 2"
        hair_shape = 1
        hair_front = 1
        hair_volume = 0
        hair_darkness = 1
        hair_bandana = 1
        for c in range(864, hair + 1):
            hair_volume += 1
            if hair_volume == 3 :
                hair_front += 1
                hair_volume = 1
                if hair_front == 7 :
                    hair_shape += 1
                    hair_front = 1
    # Ponytail 1
    elif 912 <= hair <= 947:
        hair_type = "PONYTAIL 1"
        hair_shape = 1
        hair_front = 1
        hair_volume = 0
        hair_darkness = 1
        hair_bandana = 1
        for c in range(912, hair + 1):
            hair_volume += 1
            if hair_volume == 4 :
                hair_front += 1
                hair_volume = 1
                if hair_front == 5:
                    hair_shape += 1
                    hair_front = 1
    # Ponytail 2
    elif 948 <= hair <= 983:
        hair_type = "PONYTAIL 2"
        hair_shape = 1
        hair_front = 1
        hair_volume = 0
        hair_darkness = 1
        hair_bandana = 1
        for c in range(948, hair + 1):
            hair_volume += 1
            if hair_volume == 4 :
                hair_front += 1
                hair_volume = 1
                if hair_front == 5:
                    hair_shape += 1
                    hair_front = 1
    # Dreadlocks
    elif 984 <= hair <= 1007:
        hair_type = "DREADLOCKS"
        hair_shape = 1
        hair_front = 1
        hair_volume = 0
        hair_darkness = 1
        hair_bandana = 1
        for c in range(984, hair + 1):
            hair_volume += 1
            if hair_volume == 3 :
                hair_front += 1
                hair_volume = 1
                if hair_front == 5 :
                    hair_shape += 1
                    hair_front = 1
    # Pulled back
    elif 1008 <= hair <= 1025:
        hair_type = "PULLED BACK"
        hair_shape = 1
        hair_front = 0
        hair_volume = 1
        hair_darkness = 1
        hair_bandana = 1
        for c in range(1008, hair + 1):
            hair_front += 1
            if hair_front == 7:
                hair_shape += 1
                hair_front = 1
    # Special hair
    else:
        hair_type = "SPECIAL HAIRSTYLES"
        hair_shape = hair - 1025
        hair_front = 1
        hair_volume = 1
        hair_darkness = 1
        hair_bandana = 1        

    if hair_bandana==4:
        hair_bandana=1
    hair_bandana-=1

    return [hair_type, hair_shape, hair_front, hair_volume, hair_darkness, hair_bandana]



def denormalize_hairstyle(hair_options):
    hair_type = hair_options[0]
    hair_shape = hair_options[1] - 1
    hair_front = hair_options[2] - 1
    hair_volume = hair_options[3] - 1
    hair_darkness = hair_options[4] - 1
    hair_bandana_type = hair_options[5] - 1
    if hair_type == 'BALD':
        hair_idx = hair_shape

    elif hair_type == 'BUZZ CUT':
        hair_idx = 4 + (hair_darkness) + (hair_front * 4) + (hair_shape * 20)

    elif hair_type == 'VERY SHORT 1':
        hair_idx = 84 + (hair_front) + (hair_shape * 6)

    elif hair_type == 'VERY SHORT 2':
        if 0 <= hair_shape <= 2:
            hair_idx = 108 + (hair_shape * 10) + (hair_front)
        else:
            hair_idx = 138 + ((hair_shape - 3) * 5) + (hair_front)

    elif hair_type == 'STRAIGHT 1':
        if 0 <= hair_front <= 8:
            hair_idx = 153 + hair_bandana_type + hair_volume * 3 + hair_front * 9 + hair_shape * 102
        else:
            hair_idx = 234 + hair_volume + (hair_front - 9) * 3 + hair_shape * 102

    elif hair_type == 'STRAIGHT 2':
        if 0 <= hair_front <= 1:
            hair_idx = 561 + hair_bandana_type + hair_volume * 3 + hair_front * 9 + hair_shape * 33
        else:
            hair_idx = 579 + hair_volume + (hair_front - 2) * 3 + hair_shape * 33
            
    elif hair_type == 'CURLY 1':
        if 0 <= hair_front <= 4:
            hair_idx = 660 + hair_bandana_type + hair_volume * 3 + hair_front * 9 + hair_shape * 51
        else:
            hair_idx = 705 + hair_volume + (hair_front - 5) * 3 + hair_shape * 51

    elif hair_type == 'CURLY 2':
        hair_idx = 864 + hair_volume + hair_front * 2 + hair_shape * 12

    elif hair_type == 'PONYTAIL 1':
        hair_idx = 912 + hair_volume + hair_front * 3 + hair_shape * 12

    elif hair_type == 'PONYTAIL 2':
        hair_idx = 948 + hair_volume + hair_front * 3 + hair_shape * 12

    elif hair_type == 'DREADLOCKS':
        hair_idx = 984 + hair_volume + hair_front * 2 + hair_shape * 8

    elif hair_type == 'PULLED BACK':
        hair_idx = 1008 + hair_front + hair_shape * 6

    elif hair_type == 'SPECIAL HAIRSTYLES':
        hair_idx = 1026 + hair_shape

    return hair_idx


