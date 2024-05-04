import markdown

# Your Markdown text
markdown_text = """
## java code

```java

public classs Hello
{

    public static void main(String[] args)
    {
        System.out.println("Hello World");
    } 
}
```
"""

# Convert Markdown to HTML
html = markdown.markdown(markdown_text)

print(html)