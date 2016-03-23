NAME = prelude-lml-rules
VERSION = 1.3.0rc1

clean:
	rm -rf dist build

dist: clean
	mkdir -p dist
	mkdir -p build/$(NAME)-$(VERSION)
	cp -R src/ ruleset/ COPYING README NEWS AUTHORS build/$(NAME)-$(VERSION)/
	(cd build; tar czf ../dist/$(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)/) 
