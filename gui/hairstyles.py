def hairstyle_options(self, player:Player):
    option = self.player_hair_type_combobox.get()
    if option == 'BALD':
        shape_max = 4
        shape_state = "normal"
        front_max = 1
        front_state = "disabled"
        volume_max = 1
        volume_state = "disabled"
        darkness_max = 1
        darkness_state = "disabled"
        bandana_type_max = 0
        bandana_type_state = "disabled"
        
    elif option == 'BUZZ CUT':
        shape_max = 4
        shape_state = "normal"
        front_max = 5
        front_state = "normal"
        volume_max = 1
        volume_state = "disabled"
        darkness_max = 4
        darkness_state = "normal"
        bandana_type_max = 0
        bandana_type_state = "disabled"

    elif option == 'VERY SHORT 1':
        shape_max = 4
        shape_state = "normal"
        front_max = 6
        front_state = "normal"
        volume_max = 1
        volume_state = "disabled"
        darkness_max = 1
        darkness_state = "disabled"
        bandana_type_max = 0
        bandana_type_state = "disabled"

    elif option == 'VERY SHORT 2':
        shape_max = 6
        shape_state = "normal"
        front_max = 10
        front_state = "normal"
        volume_max = 1
        volume_state = "disabled"
        darkness_max = 1
        darkness_state = "disabled"
        bandana_type_max = 0
        bandana_type_state = "disabled"

    elif option == 'STRAIGHT 1':
        shape_max = 4
        shape_state = "normal"
        front_max = 16
        front_state = "normal"
        volume_max = 3
        volume_state = "normal"
        darkness_max = 1
        darkness_state = "disabled"
        bandana_type_max = 2
        bandana_type_state = "normal"

    elif option == 'STRAIGHT 2':
        shape_max = 3
        shape_state = "normal"
        front_max = 7
        front_state = "normal"
        volume_max = 3
        volume_state = "normal"
        darkness_max = 1
        darkness_state = "disabled"
        bandana_type_max = 2
        bandana_type_state = "normal"
            
    elif option == 'CURLY 1':
        shape_max = 4
        shape_state = "normal"
        front_max = 7
        front_state = "normal"
        volume_max = 3
        volume_state = "normal"
        darkness_max = 1
        darkness_state = "disabled"
        bandana_type_max = 2
        bandana_type_state = "normal"

    elif option == 'CURLY 2':
        shape_max = 4
        shape_state = "normal"
        front_max = 1
        front_state = "disabled"
        volume_max = 1
        volume_state = "disabled"
        darkness_max = 1
        darkness_state = "disabled"
        bandana_type_max = 0
        bandana_type_state = "disabled"

    elif option == 'PONYTAIL 1':
        shape_max = 4
        shape_state = "normal"
        front_max = 6
        front_state = "normal"
        volume_max = 2
        volume_state = "normal"
        darkness_max = 1
        darkness_state = "disabled"
        bandana_type_max = 0
        bandana_type_state = "disabled"

    elif option == 'PONYTAIL 2':
        shape_max = 3
        shape_state = "normal"
        front_max = 4
        front_state = "normal"
        volume_max = 3
        volume_state = "normal"
        darkness_max = 1
        darkness_state = "disabled"
        bandana_type_max = 0
        bandana_type_state = "disabled"

    elif option == 'DREADLOCKS':
        shape_max = 3
        shape_state = "normal"
        front_max = 4
        front_state = "normal"
        volume_max = 2
        volume_state = "normal"
        darkness_max = 1
        darkness_state = "disabled"
        bandana_type_max = 0
        bandana_type_state = "disabled"

    elif option == 'PULLED BACK':
        shape_max = 3
        shape_state = "normal"
        front_max = 6
        front_state = "normal"
        volume_max = 1
        volume_state = "disabled"
        darkness_max = 1
        darkness_state = "disabled"
        bandana_type_max = 0
        bandana_type_state = "disabled"

    elif option == 'SPECIAL HAIRSTYLES':
        shape_max = 1022
        shape_state = "normal"
        front_max = 1
        front_state = "disabled"
        volume_max = 1
        volume_state = "disabled"
        darkness_max = 1
        darkness_state = "disabled"
        bandana_type_max = 0
        bandana_type_state = "disabled"

    
    self.player_hair_shape_var = IntVar()
    self.player_hair_shape_var.set(player.appearance.hair()[1])
    self.player_hair_shape_label = Label(self, text="Hair Shape")
    self.player_hair_shape_label.grid(row=23, column=0, sticky="e")
    self.player_hair_shape_spinbox = Spinbox(self, from_=1, to=shape_max, state = shape_state, textvariable=self.player_hair_shape_var)
    self.player_hair_shape_spinbox.grid(row=23, column=1, sticky="w")

    self.player_hair_front_var = IntVar()
    self.player_hair_front_var.set(player.appearance.hair()[2])
    self.player_hair_front_label = Label(self, text="Hair Front")
    self.player_hair_front_label.grid(row=24, column=0, sticky="e")
    self.player_hair_front_spinbox = Spinbox(self, from_=1, to=front_max, state = front_state, textvariable=self.player_hair_front_var)
    self.player_hair_front_spinbox.grid(row=24, column=1, sticky="w")

    self.player_hair_volume_var = IntVar()
    self.player_hair_volume_var.set(player.appearance.hair()[3])
    self.player_hair_volume_label = Label(self, text="Hair Volume")
    self.player_hair_volume_label.grid(row=25, column=0, sticky="e")
    self.player_hair_volume_spinbox = Spinbox(self, from_=1, to=volume_max, state = volume_state, textvariable=self.player_hair_volume_var)
    self.player_hair_volume_spinbox.grid(row=25, column=1, sticky="w")

    self.player_hair_darkness_var = IntVar()
    self.player_hair_darkness_var.set(player.appearance.hair()[4])
    self.player_hair_darkness_label = Label(self, text="Hair Darkness")
    self.player_hair_darkness_label.grid(row=26, column=0, sticky="e")
    self.player_hair_darkness_spinbox = Spinbox(self, from_=1, to=darkness_max, state = darkness_state, textvariable=self.player_hair_darkness_var)
    self.player_hair_darkness_spinbox.grid(row=26, column=1, sticky="w")

    self.player_hair_bandana_type_var = IntVar()
    self.player_hair_bandana_type_var.set(player.appearance.hair()[5])
    self.player_hair_bandana_type_label = Label(self, text="Hair Bandana Type")
    self.player_hair_bandana_type_label.grid(row=27, column=0, sticky="e")
    self.player_hair_bandana_type_spinbox = Spinbox(self, from_=0, to=bandana_type_max, state = bandana_type_state, textvariable=self.player_hair_bandana_type_var)
    self.player_hair_bandana_type_spinbox.grid(row=27, column=1, sticky="w")
