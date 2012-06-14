{
  'variables': {    
	'expat_Root': 'C:/Users/Toby/dev/Expat 2.1.0',
  },
  'targets': [
    {
      'target_name': 'expat',
      'sources': [
        'node-expat.cc'
      ],
      'conditions': [
        [ 'OS=="win"', {
          #we need to link to the libeay32.lib
		  'defines': [  ],
          'libraries': ['-l<(expat_Root)/bin/libexpat.lib'],
          'include_dirs': ['<(expat_Root)/Source/lib'],
        }],
        [ 'OS=="freebsd" or OS=="openbsd" or OS=="solaris" or (OS=="linux")', {
          'libraries': [],
        }],	  
	  ],
      'dependencies': [        
      ]
    }
  ]
}
