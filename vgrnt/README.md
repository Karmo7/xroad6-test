# xroad6 vagrant conf

see Vagrantfile ;)

run
 
```
vagrant up

vagrant ssh saltmaster

sudo -i

salt 'securityserver.*' cmd.run 'initctl list| grep xroad'
```

## TODO

set up center  


