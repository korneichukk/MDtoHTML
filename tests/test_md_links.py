import unittest
from src.md_links import extract_markdown_images, extract_markdown_links


class TestMarkdownExtract(unittest.TestCase):
    def test_extract_single_image(self):
        text = "Here is an image: ![Alt text](https://example.com/image.png)"
        expected = [("Alt text", "https://example.com/image.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_multiple_images(self):
        text = "![A](url1) text ![B](url2)"
        expected = [("A", "url1"), ("B", "url2")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_no_images(self):
        text = "No images here, just [a link](https://example.com)"
        self.assertEqual(extract_markdown_images(text), [])

    def test_extract_single_link(self):
        text = "Visit [Google](https://google.com)"
        expected = [("Google", "https://google.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_multiple_links(self):
        text = "[A](url1) and [B](url2)"
        expected = [("A", "url1"), ("B", "url2")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_no_links(self):
        text = "This is just an image: ![Alt](img.png)"
        self.assertEqual(extract_markdown_links(text), [])

    def test_mixed_images_and_links(self):
        text = """
        [Google](https://google.com)
        ![Image1](img1.png)
        Some text
        [Docs](https://docs.example.com)
        ![Image2](img2.jpg)
        """
        self.assertEqual(
            extract_markdown_links(text),
            [("Google", "https://google.com"), ("Docs", "https://docs.example.com")],
        )
        self.assertEqual(
            extract_markdown_images(text),
            [("Image1", "img1.png"), ("Image2", "img2.jpg")],
        )

    def test_escaped_like_syntax(self):
        text = "Escaped \\![not an image](url) and \\[not a link](url)"
        expected_links = [("not a link", "url")]
        expected_images = [("not an image", "url")]
        self.assertEqual(extract_markdown_links(text), expected_links)
        self.assertEqual(extract_markdown_images(text), expected_images)


if __name__ == "__main__":
    unittest.main()
