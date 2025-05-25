# characters/kelaita.py
# -*- coding: utf-8 -*-
character_atk = 463
character_level = 90

weapon_atk = 500
weapon_ratio = 0.12

fix_atk_ratio = 0.042 + 0.018 + 0.042 + 0.018 + 0.18 + 0.079 + 0.18 + 0.086
fix_atk = 150+100+100+40

# These are base values, skills will add to these
dis_enemy_multiplier = 0  # 伤害加成
character_dmg_amplify = 0  # 伤害加深
element_dmg_increase = 0.72  # 元素伤害加成
atk_type_dmg_increase = 0.18  # 种类伤害加成
skill_atk_ratio = 0  # 技能倍率 - Base value, will be overridden/added to by selected skills
chain_atk_ratio = 0  # 共鸣链倍率

# Define individual skill data as functions that return dictionaries
# This allows 'choose.py' to call these functions and get their specific stats

def normalAttack_1_1():
    return {'skill_atk_ratio': 0.5408, 'cooldown': 0}

def normalAttack_2_1():
    return {'skill_atk_ratio': 0.3955, 'cooldown': 0}

def normalAttack_2_2():
    return {'skill_atk_ratio': 0.3955, 'cooldown': 0}

def normalAttack_2_3():
    return {'skill_atk_ratio': 0.5273, 'cooldown': 0}

def normalAttack_Necessity_1():
    return {'skill_atk_ratio': 0.6591, 'cooldown': 0}

def normalAttack_Necessity_2():
    return {'skill_atk_ratio': 0.6008, 'cooldown': 0}

def normalAttack_Necessity_3():
    return {'skill_atk_ratio': 0.7343, 'cooldown': 0}

def normalAttack_Necessity_4():
    return {'skill_atk_ratio': 0.13993, 'cooldown': 0} # This looks like 139.93% divided by 4 based on description

def heavyAttack():
    return {'skill_atk_ratio': 0.2282 * 2 + 0.2282 * 2 + 0.6084, 'cooldown': 0}

def heavyAttack_Restricted_Strategy():
    return {'skill_atk_ratio': 0.3423 * 2 + 0.3423 * 2 + 0.9126, 'cooldown': 0, 'cooldown_reduction_violence': 6}

def aerialAttack():
    return {'skill_atk_ratio': 1.0478, 'cooldown': 0}

def aerialAttack_Polite_Greeting():
    return {'skill_atk_ratio': 1.0799 + 1.3199, 'cooldown': 0}

def dodgeCounter():
    return {'skill_atk_ratio': 1.0377 + 1.3755, 'cooldown': 0}

def resonanceSkill_Violence_Aesthetics_Initial():
    return {'skill_atk_ratio': 1.4411 * 2, 'cooldown': 14}

def resonanceSkill_Show_My_Brilliance():
    # This skill consumes shapable crystals, assuming max consumption for max damage
    return {'skill_atk_ratio': 1.1273 * 2 + 3.3818, 'cooldown': 0, 'cooldown_reset_violence': 0} # Cooldown reset handled by the skill itself

def resonanceLiberation_New_Wave_Era():
    return {'skill_atk_ratio': 4.0271, 'cooldown': 25, 'energy_cost': 125, 'dis_enemy_multiplier': 0.18} # Dis_enemy_multiplier is defense ignore

def resonanceLiberation_Death_Omen():
    return {'skill_atk_ratio': 1.8364 + 0.1450 * 4, 'cooldown': 0}

def resonanceLiberation_Fatal_End():
    return {'skill_atk_ratio': 6.4433, 'cooldown': 0}

def inherentSkill_Immaculate_Purity():
    # This skill provides utility (immunity, stamina reduction), not direct damage multipliers
    return {'skill_atk_ratio': 0, 'cooldown': 0}

def inherentSkill_Art_Above_All():
    # This skill applies dissociation, which is handled by resonanceLiberation_New_Wave_Era's dis_enemy_multiplier
    return {'skill_atk_ratio': 0, 'cooldown': 0}

def introSkill_Winter_Lament():
    return {'skill_atk_ratio': 1.7893 + 0.5965 * 2, 'cooldown': 0}

def forteCircuit_Wayward_Journey():
    return {'skill_atk_ratio': 0, 'cooldown': 0} # This is a circuit, not a direct damage skill

def forteCircuit_End_of_the_Road():
    return {'skill_atk_ratio': 0.6683 * 5 + 5.0121, 'cooldown': 22, 'cooldown_reduction_violence': 6}

def forteCircuit_Opener_Effect():
    # This effect modifies existing skills' damage, so we can add it as a multiplier
    # Assuming it's applied to resonance liberation skills if active
    return {'resonanceLiberation_New_Wave_Era_dmg_increase': 0.80,
            'resonanceLiberation_Death_Omen_dmg_increase': 0.80,
            'resonanceLiberation_Fatal_End_dmg_increase': 0.80,
            'cooldown': 0}

def outroSkill_Salutation():
    # This skill specifies damage as a percentage of ATK directly
    return {'skill_atk_ratio': 7.942, 'cooldown': 0}