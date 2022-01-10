# Atcoder

- Pythonでの長い文字列の連結は遅い
  - そのため文字列の結合をする場合はlistにアペンドしていって、最後にJOINさせる。
  - #速い
    out_list = []
    for text in text_iter:
      out_list.append(text)
    out_text = "".join(out_list)