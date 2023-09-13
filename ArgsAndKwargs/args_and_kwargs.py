def greeting_with_gender(*args, **kwargs):
    print(args)
    print(kwargs)


greeting_with_gender("hi", "hello", male="male", female="female")
