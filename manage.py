from pathlib import Path

class Manager:


    def create_readme():
        root_path = Path(__file__).parent
        # root_path.relative_to()
        # root_path.
        table_header = [
            "شماره سؤال",
            "نام سؤال",
            "لینک سؤال",
            "لینک جواب",
            ]
        with open('README.md',"w",encoding="utf8") as main_readme:
            main_readme.write("|"+"|".join(table_header)+"|"+'\n')
            main_readme.write("|-"*len(table_header)+"|"+'\n')
            index=1
            for question_path in root_path.glob(r"*/"):
                if not question_path.is_file() and not str(question_path.relative_to(root_path)).startswith("."):
                    main_readme.write(f"|{index}")
                    main_readme.write("|"+str(question_path.relative_to(root_path)))

                    with open(str(question_path.joinpath("readme.md")),"r",encoding="utf8") as local_readme:
                        main_readme.write("|"+local_readme.readline())



                    main_readme.write("|")
                    for language in question_path.glob("*"):
                        if language.is_dir():
                            solution_path = str(language.relative_to(root_path)).replace(' ','%20').replace('\\','/')
                            main_readme.write(f"[{str(language.relative_to(question_path))}]({solution_path}), ")
                    main_readme.write("|\n")

                    # print(question_path.relative_to(root_path))
                    index+=1


if __name__ == "__main__":
    Manager.create_readme()

