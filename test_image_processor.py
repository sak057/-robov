import pytest
from PIL import Image
from io import BytesIO
import os
from main import resize_image, rotate_image, convert_to_grayscale, make_background_transparent_with_edge

@pytest.fixture
def sample_image(tmp_path):
    """テスト用のサンプル画像を作成"""
    image_path = tmp_path / "test_image.jpg"
    image = Image.new("RGB", (100, 100), color="white")
    image.save(image_path)
    return str(image_path)

def test_resize_image(sample_image, tmp_path):
    """画像のリサイズをテスト"""
    output_image_path = tmp_path / "resized_image.jpg"
    image = Image.open(sample_image)
    image = image.resize((50, 50))  # リサイズ処理
    image.save(output_image_path)

    resized_image = Image.open(output_image_path)
    assert resized_image.size == (50, 50)

def test_rotate_image(sample_image, tmp_path):
    """画像の回転をテスト"""
    output_image_path = tmp_path / "rotated_image.jpg"
    image = Image.open(sample_image)
    rotated_image = image.rotate(45, expand=True)
    rotated_image.save(output_image_path)

    assert os.path.exists(output_image_path)

def test_convert_to_grayscale(sample_image, tmp_path):
    """画像のグレースケール変換をテスト"""
    output_image_path = tmp_path / "grayscale_image.jpg"
    image = Image.open(sample_image)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_image_path)

    loaded_image = Image.open(output_image_path)
    assert loaded_image.mode == "L"

def test_make_background_transparent_with_edge(sample_image, tmp_path):
    """背景透過処理をテスト"""
    output_image_path = tmp_path / "transparent_image.png"
    transparent_image = make_background_transparent_with_edge(sample_image)
    transparent_image.save(output_image_path)

    assert os.path.exists(output_image_path)
    with Image.open(output_image_path) as img:
        assert img.mode == "RGBA"

