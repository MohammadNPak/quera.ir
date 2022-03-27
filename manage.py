# -*- coding: utf-8 -*-
from pathlib import Path

class Manager:


    def create_readme():
        root_path = Path(__file__).parent
        info ="""## حل سوالات کوئرا
برای دیدن صفحه ی اصلی هر سوال در سایت کوئرا میتوانید روی نام هر سوال کلیک کنید و یا در قسمت توضیحات روی PDF کلیک کنید.
showmeyourcode.ir
        """
        table_header = [
            "شماره سؤال",
            "نام سؤال",
            "لینک جواب",
            "توضیحات",
            ]
        with open('README.md',"w",encoding="utf8") as main_readme:
            main_readme.write(info+'\n')
            main_readme.write("|"+"|".join(table_header)+"|"+'\n')
            main_readme.write("|-"*len(table_header)+"|"+'\n')
            index=1
            for question_path in root_path.glob(r"*/"):
                if not question_path.is_file() and not str(question_path.relative_to(root_path)).startswith("."):
                    main_readme.write(f"|{index}")
                    # main_readme.write("|"+str(question_path.relative_to(root_path)))

                    with open(str(question_path.joinpath("readme.md")),"r",encoding="utf8") as local_readme:
                        main_readme.write("|"+local_readme.readline())

                    main_readme.write("|")
                    for language in question_path.glob("*"):
                        if language.is_dir():
                            readme_path = str(language.relative_to(root_path)).replace(' ','%20').replace('\\','/')
                            main_readme.write(f"[{str(language.relative_to(question_path))}]({readme_path}), ")

                    main_readme.write("|")
                    for local_readmes in question_path.glob("*.md"):
                        if local_readmes.is_file():
                            readme_path = str(local_readmes.relative_to(root_path)).replace(' ','%20').replace('\\','/')
                            main_readme.write(f"[readme]({readme_path}), ")

                    for pdfs in question_path.glob("*.pdf"):
                        if pdfs.is_file():
                            pdf = str(pdfs.relative_to(root_path)).replace(' ','%20').replace('\\','/')
                            main_readme.write(f"[question's pdf]({pdf}), ")
                    main_readme.write("|\n")

                    index+=1


if __name__ == "__main__":
    Manager.create_readme()

