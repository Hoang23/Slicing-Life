
style inventory_label:
    xalign 0.2

style slot:
    background Frame("square",0, 0)
    minimum(80,80)
    maximum(80,80)
    xalign 0.5

screen inventory_screen: # call this in main script
    style_prefix "inventory"

    add "#fff" # black (#000), white (#fff)
    hbox:
        # character details

        vbox:
            xmaximum 300
            spacing 10
            label "Character" # xalign 0.5
            
            label "Health: [pc.hp]/[pc.max_hp]"
            label "Persuasion: [pc.persuasion]"
            label "Perseverance: [pc.perseverance]"
            label "Motivation: [pc.motivation]"
            label "Intelligence: [pc.intelligence]"
            label "Charisma: [pc.charisma]"

            frame:
                style "slot"
                if pc.hold["hold"] != None:
                    add pc.hold["hold"].name
                else:
                    label "hold" xalign 0.5 yalign 0.5 text_size 15

            frame: 
                style "slot"
                if pc.armor["head"] != None:
                    add pc.armor["head"].name
                else:
                    label "head" xalign 0.5 yalign 0.5 text_size 15

            # frame:
            #     style "slot"
            #     if pc.armor["chest"] != None:
            #         add pc.armor["chest"].name
            #     else: 
            #         label "chest" xalign 0.5 yalign 0.5 text_size 15


            frame: 
                style "slot"
                if pc.armor["acc"] != None:
                    add pc.armor["acc"].name
                else:
                    label "accessory" xalign 0.5 yalign 0.5 text_size 15

            frame: 
                style "slot"
                if pc.armor["outfit"] != None:
                    add pc.armor["outfit"].name
                else:
                    label "outfit" xalign 0.5 yalign 0.5 text_size 15

        # inventory grid
        vbox:
            label "Inventory" xalign 0.1 # 0.5 is the middle
            spacing 27 # in this case vertical spacing?
            grid 10 7: # 10 by 7
                for item in inventory:
                    frame:
                        style "slot"
                        if isinstance(item, KeyItem):
                            add "bg keyitem"
                        imagebutton idle item.name action SetVariable("selected_item", item)
                for i in range(len(inventory), 70):
                    frame:
                        style "slot"


        # item details
        vbox:
            
            label "Coin: [pc.coin]"
            label "Current Item" xalign 0.5

            spacing 20
            if selected_item != None:
                frame:
                    style "slot"
                    if isinstance(selected_item, KeyItem):
                        add "bg keyitem" # give different background
                    add selected_item.name
                label "Value: [selected_item.value]"

                # buttons on gui when item is selected

                if isinstance(selected_item, Consumable):
                    textbutton "Use" action Function(selected_item.use, pc) # pc as target
                if isinstance(selected_item, Weapon) or isinstance(selected_item, Armor):
                    if selected_item.is_equipped == True:
                        textbutton "Unequip" action Function(selected_item.unequip) # python function
                    else:
                        textbutton "Equip" action Function(selected_item.equip, pc) # python function

                #  only show discard button item if it is not a KeyItem
                if not isinstance(selected_item, KeyItem) and ((selected_item.is_equipped == False) or (isinstance(selected_item, Consumable))): 
                    # if it is weapon piece or armor piece: unequip the piece first 
                        
                    textbutton "Discard" action [RemoveFromSet(inventory, selected_item), SetVariable("selected_item", None)] # execute multiple function 

            
            

    textbutton "Return":  # so we can return to the original screen
        action Return()
        xalign 0.5
        yalign 0.95

