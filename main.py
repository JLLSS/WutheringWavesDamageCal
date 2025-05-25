import choose

character_atk = choose.character_atk
character_level = choose.character_level

weapon_atk = choose.weapon_atk
weapon_ratio = choose.weapon_ratio

fix_atk_ratio = choose.fix_atk_ratio
fix_atk = choose.fix_atk

dis_enemy_multiplier = choose.dis_enemy_multiplier
character_dmg_amplify = choose.character_dmg_amplify
element_dmg_increase = choose.element_dmg_increase
atk_type_dmg_increase = choose.atk_type_dmg_increase
skill_atk_ratio = choose.skill_atk_ratio
chain_atk_ratio = choose.chain_atk_ratio

res_ratio = 0
dis_res_ratio = 0
enemy_level = 90
basic_dmg_reduce_ratio = 0
extra_dmg_reduce_ratio = 0
basic_element_reduce_ratio = 0.1
enemy_dmg_amplify = 0
#基础攻击乘区
def ATK (character_atk,weapon_atk,weapon_ratio,fix_atk,fix_atk_ratio,skill_atk_ratio):
    return ((character_atk + weapon_atk )* (1 + weapon_ratio + fix_atk_ratio) + fix_atk)*skill_atk_ratio
atk = ATK(character_atk,weapon_atk,weapon_ratio,fix_atk,fix_atk_ratio,skill_atk_ratio)

#减免乘区
def enemyElementRES(res_ratio,dis_res_ratio):
    ratio_sum = res_ratio - dis_res_ratio
    if ratio_sum < 0 :
        return 1 - ratio_sum/2
    elif 0 <= ratio_sum < 0.8 :
        return 1 - ratio_sum
    else :
        return 1 / (1 + (5 * ratio_sum))
element_res = enemyElementRES(res_ratio,dis_res_ratio)

def enemyMultiplier(enemy_level,character_level,dis_enemy_multiplier): #防御乘数百分比
    return (800 + 8 * character_level) / ((800 + 8 * character_level) + ((8 * enemy_level) + 792) * (1 - dis_enemy_multiplier))
enemy_multiplier = enemyMultiplier(enemy_level,character_level,dis_enemy_multiplier)

def reduceDMG(basic_dmg_reduce_ratio,extra_dmg_reduce_ratio):
    return 1 - (basic_dmg_reduce_ratio + extra_dmg_reduce_ratio)
reduce_dmg = reduceDMG(basic_dmg_reduce_ratio,extra_dmg_reduce_ratio)

def reduceElement(basic_element_reduce_ratio,extra_dmg_reduce_ratio):
    return 1 - (basic_element_reduce_ratio + extra_dmg_reduce_ratio)
reduce_element = reduceElement(basic_element_reduce_ratio,extra_dmg_reduce_ratio)

def reducement(element_res,enemy_multiplier,reduce_dmg,reduce_element):
    return element_res * enemy_multiplier * reduce_dmg * reduce_element
reduce = reducement(element_res,enemy_multiplier,reduce_dmg,reduce_element)

#伤害加成乘区
def dmgIncrease(element_dmg_increase,atk_type_dmg_increase) :
    return 1 + (element_dmg_increase + atk_type_dmg_increase)
dmg_increase = dmgIncrease(element_dmg_increase,atk_type_dmg_increase)

def dmgAmplify(enemy_dmg_amplify,character_dmg_amplify):
    return 1 + (enemy_dmg_amplify + character_dmg_amplify)
dmg_amplify = dmgAmplify(enemy_dmg_amplify,character_dmg_amplify)

increase = dmg_increase * dmg_amplify
#结果
damage = atk * reduce * increase
print("普攻一段：",damage,end="")