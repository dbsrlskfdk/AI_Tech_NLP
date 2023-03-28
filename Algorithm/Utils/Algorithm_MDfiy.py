import configparser
import json
import re
import requests
import os


def boj_problem_parser(url):
    html = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
    html_contents = html.text

    title = re.findall("(\<span id=\"problem_title\"\>)([\s\S]+?)(\<\/span\>)", html_contents)[0][1]
    problem_description_section = re.findall("(\<section id=\"description\"  class=\"problem\-section\"\>)([\s\S]+?)(\<\/section\>)", html_contents)[0][1]
    problem_description = re.findall("(\<div id=\"problem\_description\" class=\"problem\-text\"\>)([\s\S]+?)(\<\/div\>)", problem_description_section)[0][1]
    problem_description = re.sub(r"\t|\r","", problem_description)

    input_description = re.findall("(\<div id=\"problem\_input\" class=\"problem\-text\"\>)([\s\S]+?)(\<\/div\>)", html_contents)[0][1]
    input_description = re.sub(r"\t|\r", "", input_description)

    output_description = re.findall("(\<div id=\"problem\_output\" class=\"problem\-text\"\>)([\s\S]+?)(\<\/div\>)", html_contents)[0][1]
    output_description = re.sub(r"\t|\r", "", output_description)

    markdown_contents = "# "+title+ "\n" + f"[문제 링크]({url})" + "\n" +"## " + "문제 설명" + "\n" + problem_description + "\n" + "## " + "입력" + "\n" + input_description + "\n" + "## " + "출력" + output_description

    return markdown_contents


def prog_problem_parser(url):
    html = requests.get(url, headers={"User-Agent":"Chrome/108.0.0.0"})
    html_contents = html.text

    problem_title = re.findall("(\<li class=\"nav\-item algorithm\-nav\-link algorithm\-title\">)([\s\S]+?)(\<\/li\>)", html_contents)[0][1]
    problem_title = problem_title.strip()
    problem_description = re.findall("(\<div class=\"markdown solarized\-dark\"\>)([\s\S]+?)(\<\/div\>)", html_contents)[0][1]
    problem_description_title = re.findall("(\<h6 class=\"guide\-section\-title\"\>)([\s\S]+?)(\<\/h6\>)", html_contents)[0][1]

    problem_description = re.sub(r"(\<h3\>)", "\n## ", problem_description)
    problem_description = re.sub(r"(\<\/h3\>)", "", problem_description)

    markdown_contents = f"# {problem_title}" +"\n" + f"[문제 링크]({url})"+"\n"+ f"## {problem_description_title}" +"\n"+ problem_description
    return markdown_contents


if __name__ == "__main__":
    conf = configparser.ConfigParser()
    conf.read("./Algorithm/Utils/problem_URL.conf", encoding='utf-8')

    week_num = conf['Url']['week']
    boj_prob = json.JSONDecoder().decode(conf['Url']['boj'])
    prog_prob = json.JSONDecoder().decode(conf['Url']['prog'])

    problem_dict = dict(list(boj_prob.items()) + list(prog_prob.items()))

    for i, problem_url in problem_dict.items():
        if problem_url.find('acmicpc') != -1:
            with open(os.path.join("./","Algorithm", week_num, f"Num {i}", "README.md"), mode="w", encoding="utf8") as f:
                f.write(boj_problem_parser(problem_url))
        elif problem_url.find('programmers') != -1:
            with open(os.path.join("./","Algorithm", week_num, f"Num {i}", "README.md"), mode="w", encoding="utf8") as f:
                f.write(prog_problem_parser(problem_url))
