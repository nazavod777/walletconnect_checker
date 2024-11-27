with open(
    file='const/parsed_eligible_list.txt',
    mode='r',
    encoding='utf-8'
) as file:
    eligible_list: list[str] = [row.strip().lower() for row in file]
