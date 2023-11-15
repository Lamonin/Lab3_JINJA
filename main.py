import jinja2
import math

env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
template = env.get_template("custom_list_template.html")

result_html = template.render(
    chkboxname="numbers",
    chkboxlist=['one', 'two', 'three'],
    chkboxchkd=[1, 2]
)

with open('custom_list.html', 'w', encoding='utf-8-sig') as f:
    f.write(result_html)

# Second template
template = env.get_template("functions_table_template.html")

func_list = []
for i in range(-5, 6):
    func_list.append(
        {
            "x": i,
            "f(x)": math.sin(i),
            "y(x)": math.cos(i)
        }
    )

result_html = template.render(
    funclist=func_list,
    start_row=5,
    end_row=4
)

with open('functions_table.html', 'w', encoding='utf-8-sig') as f:
    f.write(result_html)
