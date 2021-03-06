
def find_descendents_by_name(node, name) :
  return _find_descendents_by_name(node, name, [])

def _find_descendents_by_name(node, name, results):
  if isinstance(node, list) :
    for child in node :
      _find_descendents_by_name(child, name, results)

  elif isinstance(node, dict):
    for k in node :
      if name == k :
        results.append(node[k])
      else:
        _find_descendents_by_name(node[k], name, results)
  return results

if __name__ == "__main__":
  a = {"a":"b", "c": [1,2], "d":{"c":1}}
  find_descendents_by_name(a, 'c')
  find_descendents_by_name(a, 'c')
