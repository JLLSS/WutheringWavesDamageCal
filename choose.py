# choose.py
import importlib


def choose_character_and_skills():
    character_name = input("请输入角色名称 (例如: kelaita): ").strip().lower()

    try:
        character_module = importlib.import_module(f"characters.{character_name}")
        print(f"已选择角色: {character_name}")

        character_data = {
            "character_atk": character_module.character_atk,
            "character_level": character_module.character_level,
            "weapon_atk": character_module.weapon_atk,
            "weapon_ratio": character_module.weapon_ratio,
            "fix_atk_ratio": character_module.fix_atk_ratio,
            "fix_atk": character_module.fix_atk,
            "dis_enemy_multiplier": getattr(character_module, 'dis_enemy_multiplier', 0),
            "character_dmg_amplify": getattr(character_module, 'character_dmg_amplify', 0),
            "element_dmg_increase": getattr(character_module, 'element_dmg_increase', 0),
            "atk_type_dmg_increase": getattr(character_module, 'atk_type_dmg_increase', 0),
            "skill_atk_ratio": getattr(character_module, 'skill_atk_ratio', 0),
            # Base value, will be overridden/added to
            "chain_atk_ratio": getattr(character_module, 'chain_atk_ratio', 0),
        }

        # Dynamically get all callable skills (functions) from the character module
        available_skills = {
            name: func for name, func in character_module.__dict__.items()
            if callable(func) and not name.startswith('__')
               and name not in [
                   'normalAttack', 'resonanceSkill', 'resonanceLiberation',
                   'forteCircuit', 'outroSkill', 'introSkill',
                   'inherentSkill_1', 'inherentSkill_2', 'support_action'
               ]  # Exclude parent functions/support
        }
        print("\n可用的技能:")
        for i, skill_name in enumerate(available_skills.keys()):
            print(f"{i + 1}: {skill_name}")

        selected_skills = {}
        total_cooldown = 0

        while True:
            skill_choice = input("请选择要包含的技能 (输入序号，输入 'done' 完成选择, 'cancel' 取消): ").strip().lower()
            if skill_choice == 'done':
                break
            elif skill_choice == 'cancel':
                return None, None, 0
            else:
                try:
                    skill_index = int(skill_choice) - 1
                    skill_name_list = list(available_skills.keys())
                    if 0 <= skill_index < len(skill_name_list):
                        chosen_skill_name = skill_name_list[skill_index]
                        if chosen_skill_name not in selected_skills:
                            skill_func = available_skills[chosen_skill_name]

                            # Execute the skill function to get its data dictionary
                            skill_data_from_func = skill_func()

                            # Ensure it's a dictionary and get relevant info
                            if isinstance(skill_data_from_func, dict):
                                skill_info = skill_data_from_func
                                selected_skills[chosen_skill_name] = skill_info
                                total_cooldown += skill_info.get('cooldown', 0)
                                print(f"已添加技能: {chosen_skill_name}")
                            elif isinstance(skill_data_from_func, (float, int)):
                                # If a skill function directly returns a number, treat it as skill_atk_ratio
                                skill_info = {'skill_atk_ratio': skill_data_from_func, 'cooldown': 0}
                                selected_skills[chosen_skill_name] = skill_info
                                total_cooldown += skill_info.get('cooldown', 0)  # Cooldown is 0 for these
                                print(f"已添加技能: {chosen_skill_name}")
                            else:
                                print(f"无法获取技能 '{chosen_skill_name}' 的有效数据，跳过。")

                        else:
                            print(f"技能 '{chosen_skill_name}' 已选择。")
                    else:
                        print("无效的技能序号，请重新输入。")
                except ValueError:
                    print("无效的输入，请输入数字、'done' 或 'cancel'。")
                except Exception as e:  # Catch any other potential errors during skill data retrieval
                    print(f"处理技能 '{chosen_skill_name}' 时发生错误: {e}")
        return character_data, selected_skills, total_cooldown
    except ImportError:
        print(f"未找到角色 '{character_name}'。请确保角色名称正确且文件存在。")
        return None, None, 0
    except AttributeError as e:
        print(f"角色数据加载错误: {e}. 请检查角色文件中的变量名。")
        return None, None, 0