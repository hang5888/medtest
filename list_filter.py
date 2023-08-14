def list_str(data, what_str, witch_one):
  erer = [sublist for sublist in data if what_str in sublist[witch_one]]
  return erer


def list_notin_str(data, what_str, witch_one):
  erer = [sublist for sublist in data if what_str not in sublist[witch_one]]
  return erer


def list_bigger_int(data, what_int, witch_one):
  erer = [sublist for sublist in data if what_int < sublist[witch_one]]
  return erer


def list_semller_int(data, what_int, witch_one):
  erer = [sublist for sublist in data if what_int > sublist[witch_one]]
  return erer


def list_equal_int(data, what_int, witch_one):
  erer = [sublist for sublist in data if what_int == sublist[witch_one]]
  return erer


def list_notequa_lint(data, what_int, witch_one):
  erer = [sublist for sublist in data if what_int != sublist[witch_one]]
  return erer
