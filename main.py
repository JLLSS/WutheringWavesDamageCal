# main.py
# -*- coding: utf-8 -*-
import choose

def calculate_damage(character_atk, character_level,
                     weapon_atk, weapon_ratio,
                     fix_atk_ratio, fix_atk,
                     dis_enemy_multiplier, character_dmg_amplify,
                     element_dmg_increase, atk_type_dmg_increase,
                     skill_atk_ratio, chain_atk_ratio,
                     res_ratio=0, dis_res_ratio=0, enemy_level=90,
                     basic_dmg_reduce_ratio=0, extra_dmg_reduce_ratio=0,
                     basic_element_reduce_ratio=0.1, enemy_dmg_amplify=0):

    # 基础攻击乘区
    def ATK(character_atk, weapon_atk, weapon_ratio, fix_atk, fix_atk_ratio, skill_atk_ratio):
        return ((character_atk + weapon_atk) * (1 + weapon_ratio + fix_atk_ratio) + fix_atk) * skill_atk_ratio

    atk = ATK(character_atk, weapon_atk, weapon_ratio, fix_atk, fix_atk_ratio, skill_atk_ratio)

    # 减免乘区
    def enemyElementRES(res_ratio, dis_res_ratio):
        ratio_sum = res_ratio - dis_res_ratio
        if ratio_sum < 0:
            return 1 - ratio_sum / 2
        elif 0 <= ratio_sum < 0.8:
            return 1 - ratio_sum
        else:
            return 1 / (1 + (5 * ratio_sum))
    element_res = enemyElementRES(res_ratio, dis_res_ratio)

    def enemyMultiplier(enemy_level, character_level, dis_enemy_multiplier):  # 防御乘数百分比
        return (800 + 8 * character_level) / ((800 + 8 * character_level) + ((8 * enemy_level) + 792) * (1 - dis_enemy_multiplier))
    enemy_multiplier = enemyMultiplier(enemy_level, character_level, dis_enemy_multiplier)

    def reduceDMG(basic_dmg_reduce_ratio, extra_dmg_reduce_ratio):
        return 1 - (basic_dmg_reduce_ratio + extra_dmg_reduce_ratio)
    reduce_dmg = reduceDMG(basic_dmg_reduce_ratio, extra_dmg_reduce_ratio)

    def reduceElement(basic_element_reduce_ratio, extra_dmg_reduce_ratio):
        return 1 - (basic_element_reduce_ratio + extra_dmg_reduce_ratio)
    reduce_element = reduceElement(basic_element_reduce_ratio, extra_dmg_reduce_ratio)

    def reducement(element_res, enemy_multiplier, reduce_dmg, reduce_element):
        return element_res * enemy_multiplier * reduce_dmg * reduce_element
    reduce = reducement(element_res, enemy_multiplier, reduce_dmg, reduce_element)

    # 伤害加成乘区
    def dmgIncrease(element_dmg_increase, atk_type_dmg_increase):
        return 1 + (element_dmg_increase + atk_type_dmg_increase)
    dmg_increase = dmgIncrease(element_dmg_increase, atk_type_dmg_increase)

    def dmgAmplify(enemy_dmg_amplify, character_dmg_amplify):
        return 1 + (enemy_dmg_amplify + character_dmg_amplify)
    dmg_amplify = dmgAmplify(enemy_dmg_amplify, character_dmg_amplify)

    increase = dmg_increase * dmg_amplify

    # 结果
    damage = atk * reduce * increase
    return damage

if __name__ == "__main__":
    selected_character_data, selected_skills_data, total_cooldown = choose.choose_character_and_skills()

    if selected_character_data and selected_skills_data is not None:
        # Aggregate skill ratios and other modifiers from selected skills
        aggregated_skill_atk_ratio = 0
        aggregated_element_dmg_increase = 0
        aggregated_atk_type_dmg_increase = 0
        aggregated_dis_enemy_multiplier = 0 # Assume this can be aggregated if multiple skills affect it
        aggregated_character_dmg_amplify = 0 # Assume this can be aggregated

        for skill_name, skill_info in selected_skills_data.items():
            aggregated_skill_atk_ratio += skill_info.get('skill_atk_ratio', 0)
            aggregated_element_dmg_increase += skill_info.get('element_dmg_increase', 0)
            aggregated_atk_type_dmg_increase += skill_info.get('atk_type_dmg_increase', 0)
            # Add other aggregations as needed based on how skills affect the damage formula
            aggregated_dis_enemy_multiplier += skill_info.get('dis_enemy_multiplier', 0)
            aggregated_character_dmg_amplify += skill_info.get('character_dmg_amplify', 0)

        # Use the aggregated values for calculation, defaulting to character's base if not present in skills
        final_skill_atk_ratio = aggregated_skill_atk_ratio if aggregated_skill_atk_ratio else selected_character_data['skill_atk_ratio']
        final_element_dmg_increase = aggregated_element_dmg_increase if aggregated_element_dmg_increase else selected_character_data['element_dmg_increase']
        final_atk_type_dmg_increase = aggregated_atk_type_dmg_increase if aggregated_atk_type_dmg_increase else selected_character_data['atk_type_dmg_increase']
        final_dis_enemy_multiplier = aggregated_dis_enemy_multiplier if aggregated_dis_enemy_multiplier else selected_character_data['dis_enemy_multiplier']
        final_character_dmg_amplify = aggregated_character_dmg_amplify if aggregated_character_dmg_amplify else selected_character_data['character_dmg_amplify']

        damage = calculate_damage(
            character_atk=selected_character_data['character_atk'],
            character_level=selected_character_data['character_level'],
            weapon_atk=selected_character_data['weapon_atk'],
            weapon_ratio=selected_character_data['weapon_ratio'],
            fix_atk_ratio=selected_character_data['fix_atk_ratio'],
            fix_atk=selected_character_data['fix_atk'],
            dis_enemy_multiplier=final_dis_enemy_multiplier,
            character_dmg_amplify=final_character_dmg_amplify,
            element_dmg_increase=final_element_dmg_increase,
            atk_type_dmg_increase=final_atk_type_dmg_increase,
            skill_atk_ratio=final_skill_atk_ratio,
            chain_atk_ratio=selected_character_data['chain_atk_ratio']
            # Other parameters like res_ratio etc. use their default values from calculate_damage function
        )
        print(f"总伤害: {damage:.2f}")
        print(f"所选技能总冷却时间: {total_cooldown} 秒")
    else:
        print("角色或技能选择取消。")