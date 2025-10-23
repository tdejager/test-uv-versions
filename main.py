from pkg_editable import get_message
from pkg_dynamic import dynamic_message
from pkg_versioned import versioned_message


def main():
    print(get_message())
    print(dynamic_message())
    print(versioned_message())


if __name__ == "__main__":
    main()
