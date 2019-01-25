from pyquery import PyQuery as py

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-0 active"><a href="https://ask.hellobi.com/link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = py(html)

a = doc('.item-1.active a')
# <a href="https://ask.hellobi.com/link3.html"><span class="bold">third item</span></a>
print(a)
print(a.html())
print(a.attr.href)
print(a.text())