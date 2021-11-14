import face_recognition
from PIL import Image, ImageDraw


def face_rec():
    # gal_face_img = face_recognition.load_image_file("img/gal.jpg")
    # gal_face_locations = face_recognition.face_locations(gal_face_img)

    justice_league_img = face_recognition.load_image_file("img/IMG-20170622-WA0016.jpg")
    justice_league_locations = face_recognition.face_locations(justice_league_img)

    # print(gal_face_locations)
    print(justice_league_locations)
    # print(f"Found {len(gal_face_locations)} face(s)")
    print(f"Found {len(justice_league_locations)} face(s)")

    # pil_img = Image.fromarray(gal_face_img)
    # draw1 = ImageDraw.Draw(pil_img)

    # for (top, right, bottom, left) in gal_face_locations:
    #     draw1.rectangle(((left, top), (right, bottom)), outline=(173, 255, 47), width=4)

    # del draw1
    # pil_img.save("img/new_gal.png")

    pil_img2 = Image.fromarray(justice_league_img)
    draw2 = ImageDraw.Draw(pil_img2)

    for (top, right, bottom, left) in justice_league_locations:
        draw2.rectangle(((left, top), (right, bottom)), outline=(173, 255, 47), width=4)

    del draw2
    pil_img2.save("img/new_img1.png")


def extracting_faces(path):
    count = 5
    faces = face_recognition.load_image_file(path)
    faces_location = face_recognition.face_locations(faces)

    for face_loaction in faces_location:
        top, rigth, bottom, left = face_loaction

        face_img = faces[top:bottom, left:rigth]

        pil_img = Image.fromarray(face_img)
        pil_img.save(f"img/{count}_face_img.jpg")
        count += 1

    return f"Found {count} face(s)"


def compare_faces(path_1, path_2):
    img1 = face_recognition.load_image_file(path_1)
    print(img1)
    try:
        img1_encodings = face_recognition.face_encodings(img1)[0]
    except IndexError as e:
        print(e)

    img2 = face_recognition.load_image_file(path_2)

    try:
        img2_encodings = face_recognition.face_encodings(img2)[0]


    except IndexError as e:
        print(e)

    res = face_recognition.compare_faces([img1_encodings], img2_encodings)
    print(res)


def main():
    face_rec()
    # print(extracting_faces("img/IMG-20170622-WA0016.jpg"))

    # compare_faces("img/1_face_img.jpg", "img/6_face_img.jpg")


if __name__ == '__main__':
    main()
