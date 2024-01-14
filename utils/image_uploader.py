from cloudinary import uploader, CloudinaryImage


def cloudinary_upload(request, slug):
    """takes a request and a slug or name/title of object instance

    Args:
        request (_type_): takes in a request object. 
        slug (_type_): Slug is either the name or title of the object you want to get the url for. Example: "this is a blog title" becomes "this-is-a-blog-title".

    Returns:
        _type_: (string) - Cloudinary URL
    """
    image_file = request.FILES["image"]
    image_id = slug.replace(" ", "-")
    
    image = uploader.upload(image_file, public_id=image_id, unique_filename=False, overwrite=True)
    
    return image["url"]
    