NAME = prelude-lml-rules
VERSION = 1.0.0

clean:
	rm -rf dist build

dist:
	mkdir -p dist
	mkdir -p build/$(NAME)-$(VERSION)
	cp -R ruleset/ COPYING README NEWS build/$(NAME)-$(VERSION)/
	(cd build; tar czf ../dist/$(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)/) 
