xpath语法
支持层级跳转

支持布尔值
支持函数

```xpath
`//*[@id='kw'and @name='xxx']`
```

**1.基本用法**

/开头表示根路径

```xpath
	/html/body
```

//开头或者中间  表示任一层级

```
	//*[@id='kw']
```

*表示任意元素

@属性筛选

/ 在中间表示下一级

```
	/html/body
```

.表示本级

..表示上一级

**2.xpath函数**

text 获取元素内的文本（精确匹配）

contains 任意位置的包含（模糊匹配）

starts-with 开头相同 （半模糊匹配）

**3.xpath调试**

开发者工具--控制台--$x 进行xpath调试

```
$x('//input[@id='kw' and name='beifan']')
$x('//a[starts-with(text(),'新')]')
```

xpath写出来后，先在F12验证一下，然后再放入测试代码